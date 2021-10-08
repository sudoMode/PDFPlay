# -*- coding: utf-8 -*-

from argparse import ArgumentTypeError
from os.path import isdir
from os.path import join
from os.path import isfile
from os import listdir


def _is_pdf(path):
    # if not isfile(path):
    #     raise FileExistsError(f'File does not exist: {path}')
    if path.endswith('.pdf'):
        return True


class _TargetFileOTO:

    def __call__(self, path):
        if not _is_pdf(path):
            raise ArgumentTypeError(f'Expected a PDF file, received: {path}')
        return path


class _OutputFileOTO:

    def __call__(self, path):
        _is_pdf(path)
        return path


class _TargetFileOTM:

    def __call__(self, path):
        if _is_pdf(path):
            pass
        else:
            if isdir(path):
                pdfs = list(filter(_is_pdf, listdir(path)))
                path = list(map(lambda x: join(path, x), pdfs))
            else:
                raise ArgumentTypeError(f'Expected a PDF file or a directory that '
                                        f'contains PDF files, received: {path}')
        return path


class _OutputFileOTM:

    def __call__(self, path):
        if _is_pdf(path):
            raise ArgumentTypeError(f'Output location must be a directory, not a PDF '
                                    f'file: {path}')
        return path


class _WatermarkMTO:

    def __call__(self, path):
        # if not isfile(path):
        #     raise FileExistsError(f'File does not exist: {path}')
        # if not(path.endswith('.txt') or path.endswith('.rtf')):
        #     raise ArgumentTypeError(f'Watermark input must be a path to a .txt or '
        #                             f'.rtf file that contains watermark texts, '
        #                             f'received: {path}')
        return path


target_file_oto = _TargetFileOTO()
output_file_oto = _OutputFileOTO()
target_file_otm = _TargetFileOTM()
output_file_otm = _OutputFileOTM()
watermark_mto = _WatermarkMTO()
