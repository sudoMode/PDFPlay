from pathlib import Path
from os.path import join
# from reportlab.lib import pagesizes as ps
# from reportlab.lib.colors import Color


# DEFAULT_PAGE_SIZE = ps.A4
# DEFAULT_COLOR = Color(0, 0, 0, alpha=1)

# project dirs & files
BASE = Path(__file__).parent.resolve()
DATA = join(BASE, '.data')
INPUT_FILE = join(DATA, 'test_doc.pdf')

# wm settings
# FONT_NAME = 'Helvetica-Bold'
# FONT_SIZE = 25
# OPACITY = 1  # 1 means 100% opacity
# COLOR = Color(0, 0, 0, alpha=OPACITY)  # black
# POSITION_X = 0
# POSITION_Y = 0
# ROTATION_ANGLE = 0
#
# PAGES = {
#             'A4': DEFAULT_PAGE_SIZE
#         }
#
# COLORS = {
#             'black': DEFAULT_COLOR
#          }
