from os.path import join
from pathlib import Path
from pdf_play._version import VERSION

# project dirs & files
BASE = Path(__file__).parent.resolve()
DATA = join(BASE, '.data')
FONTS = ['Courier', 'Helvetica',
         'Helvetica-Bold', 'Times-Roman',
         'Times-Bold', 'Times-Italic']
FONT_SIZES = ['small', 'large', 'medium']
COLORS = ['black', 'grey', 'lightgrey', 'red', 'lightred', 'blue', 'lightblue', 'green',
          'lightgreen',
          'white']

__all__ = ['VERSION', 'COLORS', 'FONT_SIZES', 'FONTS']
