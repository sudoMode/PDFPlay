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
                          font_size=25, color='black', position_x=0,
                          position_y=0, rotation_angle=0):
        print(f'S: {locals()}')
        canvas = Canvas(self._input_buffer, pagesize=settings.PAGES[page_size])
        canvas.setFont(font_name, font_size)
        canvas.setFillColor(settings.COLORS[color])
        canvas.rotate(rotation_angle)
        canvas.drawString(position_x, position_y, text)
        canvas.save()
        self._watermark = PdfFileReader(self._input_buffer)

    def apply_watermark(self, text, output_file=None,  **style):
        if output_file is None:
            path = self._path.split('.')
            name, extension = '.'.join(path[:-1]), path[-1]
            output_file = f'{name}_wm.{extension}'
        self._create_watermark(text, **style)
        for i in range(self._input.getNumPages()):
            page = self._input.getPage(i)
            page.mergePage(self._watermark.getPage(0))
            self._out.addPage(page)
        print('here')

        with open(output_file, 'wb') as f:
            self._out.write(f)
        self._input.stream.close()


def _test():
    pdf = PDF(settings.INPUT_FILE)
    pdf.apply_watermark('test watermark!')


if __name__ == '__main__':
    _test()
