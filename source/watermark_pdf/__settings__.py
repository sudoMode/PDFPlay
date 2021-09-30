from pathlib import Path
from os.path import join
from reportlab.lib import pagesizes as ps
from reportlab.lib.colors import Color


DEFAULT_PAGE_SIZE = ps.A4
DEFAULT_COLOR = Color(0, 0, 0, alpha=1)

# project dirs & files
BASE = Path(__file__).parent.resolve()
DATA = join(BASE, '.data')
INPUT_FILE = join(DATA, 'test_doc.pdf')

# wm settings
FONT_NAME = 'Helvetica-Bold'
FONT_SIZE = 100
OPACITY = 0.25  # 1 means 100% opacity
COLOR = Color(100, 0, 0, alpha=OPACITY)  # light red
POSITION_X = 1000
POSITION_Y = 700
ROTATION_ANGLE = 30

PAGES = {
            'A4': DEFAULT_PAGE_SIZE
        }

COLORS = {
            'black': DEFAULT_COLOR
         }
