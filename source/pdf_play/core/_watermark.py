from io import BytesIO
from math import sqrt

from PyPDF4.pdf import PdfFileReader
from reportlab.pdfgen.canvas import Canvas

from reportlab.lib.colors import Color


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
        rotation = 0
        if self._text_alignment == 'diagonal':
            rotation = 45
        if self._text_alignment == 'vertical':
            rotation = 90
        self._rotation = rotation

    def _set_max_length(self):
        length = self._page_size[0]
        if self._text_alignment == 'diagonal':
            length = round(sqrt(self._page_size[0]**2 + self._page_size[1]**2)) * .8
        if self._text_alignment == 'vertical':
            length = self._page_size[1]
        self._max_length = length

    def _set_font_size(self):
        if self._font_size == 'small':
            self._font_size = 15
        if self._font_size == 'medium':
            self._font_size = 30
        if self._font_size == 'large':
            self._font_size = 45
        # size = self._max_length * .5
        # if self._font_size == 'small':
        #     size = self._max_length * .3
        # if self._font_size == 'large':
        #     size = self._max_length * .8
        # font_size = 0
        # while True:
        #     font_size += 5
        #     width = self._canvas.stringWidth(self._text, self._font_name, font_size)
        #     if width > size:
        #         break
        # self._text_width = width
        # self._font_size = font_size

    def _set_color(self):
        self._color = Color()

    def _set_position(self):
        print('PD: ', self._page_size)
        print('XX: ', type(self._x), self._y, self._rotation)
        if self._position_x == 'center':
            self._x = round(self._page_size[0] // 2)
            print('XX2: ', type(self._x), self._y, self._rotation)
        if self._position_y == 'center':
            self._y = round(self._page_size[1] // 2)
        print('XX3: ', self._x, self._y, self._rotation)
        print('XX4: ', type(self._x), self._y, self._rotation)
        if self._text_alignment == 'diagonal':
            self._x += self._rotation * 5
            self._y -= self._rotation * 7

    def _update_canvas(self):
        self._canvas.setPageSize(self._page_size)
        self._canvas.setFont(self._font_name, self._font_size)
        self._canvas.setFillColor(self._color)
        self._canvas.rotate(self._rotation)
        self._canvas.drawCentredString(self._x, self._y, self._text)
        self._canvas.save()

    def _update_style(self):
        self._set_rotation()
        self._set_max_length()
        self._set_font_size()
        self._set_color()
        self._set_position()

    def unload(self):
        watermarked_pdf = PdfFileReader(self._buffer)
        return watermarked_pdf.getPage(0)
