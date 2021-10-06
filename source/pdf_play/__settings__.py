from os.path import join
from pathlib import Path

# project dirs & files
BASE = Path(__file__).parent.resolve()
DATA = join(BASE, '.data')
FONTS = ['Courier', 'Courier-Bold', 'Courier-BoldOblique', 'Courier-Oblique', 'Helvetica',
         'Helvetica-Bold', 'Helvetica-BoldOblique', 'Helvetica-Oblique',
         'Times-Bold', 'Times-BoldItalic', 'Times-Italic', 'Times-Roman']
