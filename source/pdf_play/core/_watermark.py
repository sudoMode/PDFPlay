from io import BytesIO

from PyPDF4.pdf import PdfFileReader
from reportlab.pdfgen.canvas import Canvas

from pdf_play.core import __settings__ as settings


class WatermarkStyle:

    def __init__(self, page_size='A4', font_name='Helvetica', font_size=25,
                 rotation=0, position_x=0, position_y=0, color='black',
                 transparency=0):
        self.font_name = settings.get_font(font_name)
        self.font_size = font_size
        self.rotation = rotation
        self.position_x = position_x
        self.position_y = position_y
        self.page_size = settings.get_page(page_size)
        self.color = settings.get_color(color, transparency)


class Watermark:

    def __init__(self, text, **style):
        self.text = text
        self.style = WatermarkStyle(**style)
        self._load()

    def _load(self):
        self._buffer = BytesIO()
        canvas = Canvas(self._buffer, pagesize=self.style.page_size)
        canvas.setFont(self.style.font_name, self.style.font_size)
        canvas.setFillColor(self.style.color)
        canvas.rotate(self.style.rotation)
        canvas.drawString(self.style.position_x, self.style.position_y, self.text)
        canvas.save()
        self._canvas = canvas

    def unload(self):
        watermarked_pdf = PdfFileReader(self._buffer)
        return watermarked_pdf.getPage(0)
