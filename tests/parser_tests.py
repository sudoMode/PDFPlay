import json
from os.path import join
from unittest import TestCase
from unittest import main

from pdf_play.helpers._parser import parse_user_args
from tests import DATA


class ParserTests(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = DATA

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mto(self):
        expected_watermark_input = {
            "Name 2": "Name 2",
            "Name 3": "Name 3",
            "Name 4": "Name 4",
            "Name 5": "Name 5",
            "Name 6": "Name 6"
        }
        tf = join(self.data, 'sample_target.csv')
        i = join(self.data, 'sample6.pdf')
        command = ['watermark', 'mto', '-tf', tf, '-i', i]
        args = vars(parse_user_args(command))
        print(json.dumps(args, indent=2, sort_keys=True))
        self.assertDictEqual(args['watermark_input'], expected_watermark_input)


if __name__ == '__main__':
    main()
