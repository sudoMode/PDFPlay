from io import BytesIO
from math import atan
from math import degrees
from math import sqrt

from PyPDF4.pdf import PdfFileReader
from reportlab.lib.colors import Color
from reportlab.pdfgen.canvas import Canvas
from pdf_play.core import __settings__ as settings


# noinspection PyTypeChecker
class Watermark:

    def __init__(self, text, page_size='A4', font_name='Helvetica-Bold',
                 font_size='medium',
                 text_alignment='diagonal', font_color='black', position_x='center',
                 position_y='center', verbose=False, debug=False):
        # TODO: assert value check
        # TODO: cleanup
        self._page_size = page_size
        self._font_name = font_name
        self.font_size = font_size
        self._font_size = 50
        self._text_alignment = text_alignment
        self._color = font_color
        self._text = text
        self._position_x = position_x
        self._position_y = position_y
        self.verbose = verbose
        self.debug = debug
        self._x, self._y = self._page_size
        self._d = int(sqrt(self._x ** 2 + self._y ** 2))
        self._init_canvas()
        self._update_style()
        # self._update_canvas()

    def _init_canvas(self):
        self._buffer = BytesIO()
        self._canvas = Canvas(self._buffer)

    def _set_rotation(self):
        x, y = list(map(float, self._page_size))
        rotation = 0
        if self._text_alignment == 'diagonal':
            rotation = round(degrees(atan(y / x)))
        if self._text_alignment == 'vertical':
            rotation = 90
        self._rotation = rotation

    def _set_max_length(self):
        """
            80% of axis length
            depends on text alignment:
                - horizontal: x-axis length
                - vertical: y-axis length
                - diagonal: diagonal length
        """
        lengths = dict(horizontal=self._x, vertical=self._y, diagonal=self._d)
        length = lengths[self._text_alignment]
        self._max_length = int(length * .8)

    def _set_font_size(self):
        x, y = self._page_size
        max_width = round(self._max_length * .5)
        max_font = x * .1
        if self.font_size == 'medium':
            max_width = round(self._max_length * .75)
            max_font = x * .2
        if self.font_size == 'large':
            max_width = round(self._max_length)
            max_font = x * .3
        size = 5

        while True:
            width = self._canvas.stringWidth(self._text,
                                             fontName=self._font_name,
                                             fontSize=size)
            if width >= max_width or size >= max_font:
                break
            size += 5
        self._font_size = size
        self._width = width

    def _set_color(self):
        color = settings.COLORS[self._color]
        self._red = color['red'] / 255
        self._green = color['green'] / 255
        self._blue = color['blue'] / 255
        self._alpha = color['alpha']

    def _set_position(self):
        # set to origin
        self._x = 0
        self._y = 0

    def _update_canvas(self):
        # update canvas attrs
        self._canvas.setPageSize(self._page_size)
        self._canvas.setFont(self._font_name, self._font_size)
        self._canvas.setFillColor((self._red, self._green, self._blue), alpha=self._alpha)
        # TODO: object attrs
        x, y = list(map(int, self._page_size))
        cx, cy = (x // 2), (y // 2)  # - (self._font_size * 2)
        # set origin to center of the page
        self._canvas.translate(cx, cy)
        self._canvas.rotate(self._rotation)
        x, y = (0, 0)
        self._canvas.drawCentredString(x, y,
                                       'a really long email id @ gmail.com but it'
                                       ' needs to be longer')
        # self._canvas.drawCentredString(self._x, -.25 * self._font_size,
        #                                self._text)
        # self._canvas.save()

    def _update_style(self):
        self._set_max_length()
        self._set_rotation()
        self._set_font_size()
        self._set_color()
        # self._set_position()

    def _calculate_font_size(self, text=None, font=None):
        if text is None:
            text = self._text
        if font is None:
            font = self._font_name
        factors = dict(small=.3, medium=.5, large=.7)
        max_width = int(self._max_length * factors[self.font_size])
        size = 2
        while True:
            width = self._canvas.stringWidth(text, font, size)
            if width > max_width or size > max_width*.2:
                break
            size += 2
        return size

    def _draw_watermark(self):
        """
            update canvas style
            draw watermark text
        """
        texts = self._text.splitlines()
        self._canvas.setPageSize(self._page_size)
        self._canvas.setFont(self._font_name, self._font_size)
        self._canvas.setFillColor((self._red, self._green, self._blue), alpha=self._alpha)
        # set origin to center of the page
        self._canvas.translate(self._page_size[0] // 2, self._page_size[1] // 2)
        self._canvas.rotate(self._rotation)
        font_size = self._calculate_font_size(max(texts, key=len))
        x, y = (0, (len(texts)//2) * (font_size*.75))
        for i, text in enumerate(texts):
            self._canvas.setFontSize(font_size)
            self._canvas.drawCentredString(x, y, text)
            y -= (font_size * .8) + 10
        self._canvas.save()

    def unload(self):
        self._draw_watermark()
        watermarked_pdf = PdfFileReader(self._buffer)
        return watermarked_pdf.getPage(0)
