from io import BytesIO

from PyPDF4.pdf import PdfFileReader
from PyPDF4.pdf import PdfFileWriter
from reportlab.pdfgen.canvas import Canvas

from watermark_pdf import __settings__ as settings


class PDF:

    def __init__(self, path):
        self._path = path
        self._input = PdfFileReader(self._path)
        self._out = PdfFileWriter()
        self._input_buffer = BytesIO()
        self._watermark = None

    @staticmethod
    def _save_file(path, data, mode='wb'):
        with open(path, mode=mode) as f:
            f.write(data)

    def _create_watermark(self, text, page_size='A4', font_name='Helvetica-Bold',
                          font_size=10, color='black', position_x=0,
                          position_y=0, rotation_angle=0):
        canvas = Canvas(self._input_buffer, pagesize=settings.PAGES[page_size])
        canvas.setFont(font_name, font_size)
        canvas.setFillColor(settings.COLORS[color])
        canvas.rotate(rotation_angle)
        canvas.drawString(position_x, position_y, text)
        canvas.save()
        self._watermark = PdfFileReader(self._input_buffer)

    def apply_watermark(self, text, **style):
        self._create_watermark(text, **style)
        for i in range(self._input.getNumPages()):
            page = self._input.getPage(i)
            page.mergePage(self._watermark.getPage(0))
            self._out.addPage(page)
        print('here')

        with open('wmed.pdf', 'wb') as f:
            self._out.write(f)
        self._input.stream.close()


file = '/Users/mandeepsingh/dev/k2q/projects/WatermarkPDF/source/watermark_pdf/.data/' \
       'test_doc.pdf'
pdf = PDF(file)
style = dict(font_name='Helvetica-Bold', font_size=100,
             color='black', rotation_angle=0, position_x=0, position_y=0)
pdf.apply_watermark('wm testststs', **style)
