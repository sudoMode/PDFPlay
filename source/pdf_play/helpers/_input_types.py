# -*- coding: utf-8 -*-

from argparse import ArgumentTypeError
from os.path import isdir
from os.path import isfile
from os.path import sep

from pdf_play.helpers import utils


class _TargetFileOTO:

    def __call__(self, path):
        if not isfile(path):
            raise ArgumentTypeError(f'File does not exits: {path}')
        if not utils.is_pdf(path):
            msg = f'Given target file does not appear to be a PDF: {path}'
        return path


class _OutputFileOTO:

    def __call__(self, path):
        print(f'P: {path}')
        if not _is_pdf(path):
            name_and_extension = path.split(sep)[-1].split('.')
            if len(name_and_extension) == 2:
                extension = name_and_extension[-1]
                if extension != 'pdf':
                    raise ArgumentTypeError(f'Expected a PDF file, received: {path}')
        return path


class _TargetFileOTM:

    def __call__(self, path):
        if utils.is_pdf(path):
            if not isfile(path):
                raise ArgumentTypeError(f'File does not exist: {path}')
        else:
            if not isdir(path):
                raise ArgumentTypeError(f'Expected a PDF file or a directory that '
                                        f'contains PDF files, received: {path}')
        return path


class _OutputFileOTM:

    def __call__(self, path):
        if isfile(path):
            raise ArgumentTypeError(f'Output location must be a directory, not a file: '
                                    f'{path}')
        name_and_extension = path.split(sep)[-1].split('.')
        if len(name_and_extension) == 2:
            raise ArgumentTypeError(f'Output location must be a directory, not a file: '
                                    f'{path}')
        return path


class _WatermarkMTO:

    def __call__(self, path):
        supported = ['.txt']
        if not isfile(path):
            raise ArgumentTypeError(f'Provide path to a valid file to read watermark '
                                    f'texts, given file does not exist: {path}')
        if not any(map(lambda x: x == path[-len(x):], supported)):
            raise ArgumentTypeError(f'Bad input for watermark file: {path}, '
                                    f'please check supported file types: {supported}')
        return path


target_file_oto = _TargetFileOTO()
output_file_oto = _OutputFileOTO()
target_file_otm = _TargetFileOTM()
output_file_otm = _OutputFileOTM()
watermark_mto = _WatermarkMTO()
