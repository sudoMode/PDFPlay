from pathlib import Path
from os.path import join


# project dirs & files
BASE = Path(__file__).parent.resolve()
DATA = join(BASE, '.data')
INPUT_FILE = join(DATA, 'test_doc.pdf')
