from unittest import TestCase
from unittest import main
from pdf_play import watermark

from os.path import join

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
        target_file = join(self.input_dir, 'test_doc.pdf')
        wm_text = 'a test watermark!!'
        output_file = 'test_watermarked'
        watermark(wm_text, target_file, output_file)


if __name__ == '__main__':
    main()
