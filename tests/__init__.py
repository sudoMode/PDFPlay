from os import listdir
from os.path import isfile
from os.path import join
from pathlib import Path
from unittest import TestCase
from unittest import main

from pdf_play import watermark

DATA = join(Path(__file__).parent.resolve(), '.data')


class WatermarkTests(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.input_dir = '.data'

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_watermark(self):
        wm_text = 'a test watermark!!!'
        target_files = list(filter(lambda x: x.endswith('.pdf'), listdir(self.input_dir)))
        for i in range(len(target_files)):
            file = target_files[i]
            target_file = join(self.input_dir, file)
            output_file = join(self.input_dir, f'wm_{i + 1}.pdf')
            status = watermark(wm_text, target_file, output_file)
            self.assertTrue(status)
            self.assertTrue(isfile(output_file))

    def test_excel(self):
        pass


if __name__ == '__main__':
    main()
