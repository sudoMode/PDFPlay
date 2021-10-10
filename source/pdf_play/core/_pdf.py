from PyPDF4.pdf import PdfFileReader
from PyPDF4.pdf import PdfFileWriter

from pdf_play.core._watermark import Watermark


class PDF:

    def __init__(self, debug=False):
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
        style['page_size'] = self._target.getPage(0).mediaBox[-2:]
        watermark = Watermark(self._watermark_text, **style)
        self._watermark = watermark.unload()
        self._watermark_is_loaded = True

    def _load_watermark(self, text, target_file, out_file, **style):
        try:
            self._set_watermark_text(text)
            self._set_in_path(target_file)
            self._set_out_path(out_file)
            self._set_watermark(**style)
        except Exception as e:
            print(f'Error: {e}')
            if self._debug:
                raise e

    def apply_watermark(self, text, target_file, out_file=None, **style):
        self._load_watermark(text, target_file, out_file, **style)
        if self._watermark_is_loaded:
            for i in range(self._target.getNumPages()):
                page = self._target.getPage(i)
                page.mergePage(self._watermark)
                self._out.addPage(page)

            with open(self._out_path, 'wb') as f:
                self._out.write(f)
            self._target.stream.close()


def _test():
    pdf = PDF()
    path = ''
    pdf.apply_watermark('test watermark!', path)


if __name__ == '__main__':
    _test()
