from PyPDF4.pdf import PdfFileReader
from PyPDF4.pdf import PdfFileWriter

from pdf_play.core._watermark import Watermark


class PDF:

    def __init__(self, debug=False):
        # TODO: think
        self._in_path = None
        self._target = None
        self._out_path = None
        self._out = None
        self._debug = debug
        self._watermark_text = ''
        self._watermark_is_loaded = False
        self._reader = PdfFileReader
        self._writer = PdfFileWriter

    def _reset(self, **kwargs):
        for key, value in kwargs.items():
            if value is None:
                raise AttributeError(f'{key} can not be None')
            setattr(self, key, value)

    def _set_in_path(self, path):
        assert isinstance(path, str), f'File path must be a string, received: {path}'
        if path and path != self._in_path:
            self._in_path = path
        self._target = PdfFileReader(self._in_path)

    def _set_out_path(self, path=None):
        if path is None:
            if self._in_path is not None:
                split = self._in_path.split('.')
                name, extension = '.'.join(split[:-1]), split[-1]
                path = f'{name}_watermarked.{extension}'
        else:
            if not isinstance(path, str):
                raise TypeError(f'Output path must be a string, received: {path}')
            if not path.endswith('.pdf'):
                raise TypeError(f'Output file must be a PDF, received: {path}')
        self._out_path = path
        self._out = PdfFileWriter()

    def _set_watermark_text(self, text=''):
        self._watermark_text = text

    def _set_watermark(self, **style):
        page_size = list(map(int, self._target.getPage(0).mediaBox[-2:]))
        font_name = style.get('font_name', 'Helvetica-Bold')
        font_size = style.get('font_size', 'large')
        font_color = style.get('font_color', 'lightred')
        text_alignment = style.get('text_alignment', 'diagonal')
        watermark = Watermark(self._watermark_text, page_size=page_size,
                              font_name=font_name, font_size=font_size,
                              font_color=font_color, text_alignment=text_alignment)
        self._watermark = watermark.unload()
        self._watermark_is_loaded = True

    def _load_watermark(self, wm_text, file_to_watermark, file_to_save_it_as, **style):
        try:
            self._set_watermark_text(wm_text)
            self._set_in_path(file_to_watermark)
            self._set_out_path(file_to_save_it_as)
            self._set_watermark(**style)
        except Exception as e:
            print(f'Error: {e}')
            if self._debug:
                raise e

    def apply_watermark(self, wm_text, file_to_watermark, file_to_save_it_as, **style):
        self._load_watermark(wm_text, file_to_watermark, file_to_save_it_as, **style)
        if self._watermark_is_loaded:
            for i in range(self._target.getNumPages()):
                page = self._target.getPage(i)
                page.mergePage(self._watermark)
                self._out.addPage(page)
            with open(self._out_path, 'wb') as f:
                self._out.write(f)
            self._target.stream.close()


def _test():
    pdf = PDF(debug=True)
    text = 'watermark text 1' \
           '\nwatermark text 2' \
           '\nwatermark text 3' \
           '\nwatermark text 4' \
           '\nwatermark text 5'
    path = '/Users/mandeepsingh/dev/projects/py/PDFPlay/tests/.data/sample6.pdf'
    out = '/Users/mandeepsingh/dev/projects/py/PDFPlay/tests/.data/sample6 wm.pdf'

    pdf.apply_watermark(text, path, out)


if __name__ == '__main__':
    _test()
