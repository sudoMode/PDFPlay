from PyPDF4.pdf import PdfFileReader
from PyPDF4.pdf import PdfFileWriter

from watermark_pdf.__settings__ import COLORS
from watermark_pdf.__settings__ import DEFAULT_COLOR
from watermark_pdf.__settings__ import DEFAULT_PAGE_SIZE
from watermark_pdf.__settings__ import PAGES
from watermark_pdf.core.water_mark import Watermark

__all__ = ['COLORS', 'DEFAULT_COLOR', 'DEFAULT_PAGE_SIZE', 'PAGES', 'PdfFileReader',
           'PdfFileWriter', 'Watermark']
