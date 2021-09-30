from io import BytesIO

from reportlab.pdfgen.canvas import Canvas

from watermark_pdf.core import COLORS
from watermark_pdf.core import DEFAULT_COLOR
from watermark_pdf.core import DEFAULT_PAGE_SIZE
from watermark_pdf.core import PAGES
from watermark_pdf.core import PdfFileReader


class Watermark:

    def __init__(self, text='wm text', page_size='A4', font_name='Helvetica-Bold',
                 font_size=50, color='black', rotation_angle=45, position_x=100,
                 position_y=100):
        # super(Watermark, self).__init__()
        self.text = text
        self.buffer = BytesIO()
        self.page_size = PAGES.get(page_size, DEFAULT_PAGE_SIZE)
        self.color = COLORS.get(color, DEFAULT_COLOR)
        self.font_name = font_name
        self.font_size = font_size
        self.position_x = position_x
        self.position_y = position_y
        self.rotation_angle = rotation_angle
        self._load_canvas()

    def _load_canvas(self):
        canvas = Canvas(self.buffer)
        canvas.setPageSize(PAGES.get(self.page_size, DEFAULT_PAGE_SIZE))
        canvas.setFont(self.font_name, self.font_size)
        canvas.setFillColor(COLORS.get(self.color, DEFAULT_COLOR))
        canvas.rotate(self.rotation_angle)
        canvas.drawString(self.position_x, self.position_y, self.text)
        canvas.save()
        self.canvas = canvas

    def _reset(self, **kwargs):
        """
            to update the object
            :param kwargs:
            :type kwargs:
            :return:
            :rtype:
        """
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

    def unload(self):
        return PdfFileReader(self.buffer)
