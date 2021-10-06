from argparse import Action
from os import makedirs
from os.path import isdir


def _flatten(nested_list):
    values = []
    for i in nested_list:
        if isinstance(i, list):
            for j in i:
                values.append(j)
        else:
            values.append(i)
    return values


class _TargetFileOTO(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


class _OutputFileOTO(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


class _TargetFileOTM(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        values = _flatten(values)
        setattr(namespace, self.dest, values)


class _OutputFileOTM(Action):

    def __call__(self, parser, namespace, values, option_string=None):
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
