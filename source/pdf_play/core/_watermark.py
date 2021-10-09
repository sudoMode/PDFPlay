from io import BytesIO
import math
from PyPDF4.pdf import PdfFileReader
from reportlab.pdfgen.canvas import Canvas

from reportlab.lib.colors import Color
from math import tanh


# noinspection PyTypeChecker
class Watermark:

    def __init__(self, text, page_size='A4', font_name='Helvetica-Bold',
                 font_size='medium',
                 text_alignment='diagonal', color='black', position_x='center',
                 position_y='center'):
        # TODO: think...
        self._page_size = page_size
        self._font_name = font_name
        self._font_size = font_size
        self._text_alignment = text_alignment
        self._color = color
        self._text = text
        self._position_x = position_x
        self._position_y = position_y
        self._x, self._y = 0, 0
        self._init_canvas()
        self._update_style()
        self._update_canvas()

    def _init_canvas(self):
        self._buffer = BytesIO()
        self._canvas = Canvas(self._buffer)

    def _set_rotation(self):
        x, y = list(map(float, self._page_size))
        rotation = 0
        if self._text_alignment == 'diagonal':
            rotation = round(math.degrees(math.atan(y / x)))
        if self._text_alignment == 'vertical':
            rotation = 90
        self._rotation = rotation

    def _set_max_length(self):
        x, y = list(map(int, self._page_size))
        length = round(x * .8)
        if self._text_alignment == 'diagonal':
            length = round(math.sqrt(x**2 + y**2) * .8)
        if self._text_alignment == 'vertical':
            length = round(y * .8)
        self._max_length = length

    def _calculate_font_size(self):
        print('called')
        x, y = list(map(int, self._page_size))
        max_width = round(self._max_length * .5)
        max_font = x*.1
        if self._font_size == 'medium':
            max_width = round(self._max_length * .75)
            max_font = x*.2
        if self._font_size == 'large':
            max_width = round(self._max_length)
            max_font = x*.3
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
        print(f'Font Size: {size} | Width: {width} | Max: {max_width} | M:'
              f' {self._max_length}')

    def _set_font_size(self):
        self._calculate_font_size()

    def _set_color(self):
        self._color = Color()

    def _set_position(self):
        self._x = 0  # round(self._page_size[0] // 2)
        self._y = 0  # round(self._page_size[1] // 2)
        if self._text_alignment == 'horizontal':
            pass
        if self._text_alignment == 'diagonal':
            pass
            # self._x += self._x
            # self._y -= self._y

    def _update_canvas(self):
        self._canvas.setPageSize(self._page_size)
        self._canvas.setFont(self._font_name, self._font_size)
        self._canvas.setFillColor(self._color)
        # if self._text_alignment == 'diagonal':
        x, y = list(map(int, self._page_size))
        self._canvas.translate(x // 2, y // 2)
        self._canvas.rotate(self._rotation)
        self._canvas.drawCentredString(self._x, -.25 * self._font_size,
                                       self._text)
        self._canvas.save()

    def _update_style(self):
        self._set_max_length()
        self._set_rotation()
        self._set_font_size()
        self._set_color()
        self._set_position()

    def unload(self):
        watermarked_pdf = PdfFileReader(self._buffer)
        return watermarked_pdf.getPage(0)
