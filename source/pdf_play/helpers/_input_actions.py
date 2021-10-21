from argparse import Action
from os import listdir
from os import makedirs
from os.path import isdir
from os.path import isfile
from os.path import join
from os.path import sep
from pathlib import Path
import pandas as pd

from pdf_play.helpers import utils


class _WatermarkText(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, ' '.join(values))


class _TargetFileOTO(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


class _OutputFileOTO(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        base = Path(values).parent.resolve()
        if not isdir(base):
            makedirs(base)
        if not values.endswith('.pdf'):
            values += '.pdf'
        setattr(namespace, self.dest, values)


class _TargetFileOTM(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        values_ = []
        for value in values:
            if isdir(value):
                pdfs = list(map(lambda x: join(value, x), filter(utils.is_pdf, listdir(
                    value))))
                values_.extend(pdfs)
            else:
                values_.append(value)
        values = list(set(values_))
        setattr(namespace, self.dest, values)


class _OutputFileOTM(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        base = Path(values).parent.resolve()
        target = values.split(sep)[-1]
        existing_dirs = len(list(filter(lambda x: target in x, listdir(base))))
        if existing_dirs:
            values = join(base, f'{target}({existing_dirs + 1})')
        else:
            values = join(base, target)
        if not isdir(values):
            makedirs(values)
        setattr(namespace, self.dest, values)


class _WatermarkMTO(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


class _WatermarkMTOFile(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        """read input from a file CSV/Excel file
            return dataframe
            """
        setattr(namespace, self.dest, values)


class _FontSizeAction(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        if values not in ['small', 'medium', 'large']:
            values = int(values)
        setattr(namespace, self.dest, values)


target_file_oto = _TargetFileOTO
output_file_oto = _OutputFileOTO
target_file_otm = _TargetFileOTM
output_file_otm = _OutputFileOTM
watermark_mto_file = _WatermarkMTOFile
watermark_mto = _WatermarkMTO
watermark_text = _WatermarkText
font_size_action = _FontSizeAction
