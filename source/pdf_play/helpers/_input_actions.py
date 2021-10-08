from argparse import Action
from os import makedirs
from os import listdir
from os.path import isdir
from os.path import isfile
from os.path import join
from os.path import sep
from pathlib import Path


def _flatten(nested_list):
    values = []
    for i in nested_list:
        if isinstance(i, list):
            for j in i:
                values.append(j)
        else:
            values.append(i)
    return values


class _WatermarkText(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        print('')
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
        values = _flatten(values)
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
        with open(values, 'r') as f:
            setattr(namespace, self.dest, f.read().splitlines())


target_file_oto = _TargetFileOTO
output_file_oto = _OutputFileOTO
target_file_otm = _TargetFileOTM
output_file_otm = _OutputFileOTM
watermark_mto = _WatermarkMTO
watermark_text = _WatermarkText
