#!/usr/bin/local/python3.9
# -*- coding: utf-8 -*-

"""
    Builds CLI options
"""

from argparse import ArgumentParser
from os import listdir
from os.path import isfile
from os.path import isdir
from os import makedirs
from os.path import sep
from pathlib import Path

from pdf_play.helpers import _input_actions as actions
from pdf_play.helpers import _input_types as types


def _validate_otm(args):
    if args.output_file is None:
        args.output_file = 'watermarked'
        if not isdir(args.output_file):
            print('User did not provide an output location, a directory called '
                  '"watermarked" will be created to store all the watermarked PDF(s).')
            makedirs(args.output_file)


def _validate_oto(args):
    if isfile(args.output_file):
        print(f'An output file with the same name already exists: {args.output_file}')
        _input = input('Would you like to over-write the same? (yes/no): ')
        if _input != 'yes':
            base = Path(args.output_file).parent.resolve()
            file_name = args.output_file.split(sep)[-1]
            name, extension = file_name.split('.')
            total_files = len(list(filter(lambda x: name in x and extension in x, listdir(
                base))))
            split = args.output_file.split('.')
            name, extension = sep.join(split[:-1]), split[-1]
            args.output_file = f'{name}({total_files + 1}).{extension}'


def _update_args(args):
    if args.type == 'oto':
        _validate_oto(args)
    if args.type == 'otm':
        _validate_otm(args)
    return args


def parse_user_args(command=None):
    try:
        parser = ArgumentParser(prog='pdf_play',
                                description='Play with your PDF documents!')
        commands = parser.add_subparsers(dest='command')
        watermark = commands.add_parser('watermark', help='WM help!',
                                        description='WM des!')
        sub_commands = watermark.add_subparsers(dest='type')
        oto = sub_commands.add_parser('oto', help='one to one help')
        oto.add_argument('--text', '-t', type=str, default='PDFPlay', dest='text',
                         help='watermark text')
        oto.add_argument('--input', '-i', default=None, type=types.target_file_oto,
                         action=actions.target_file_oto, dest='target_file',
                         help='target file')
        oto.add_argument('--output', '-o', default=None, type=types.output_file_oto,
                         action=actions.output_file_oto, dest='output_file',
                         help='output file')
        oto.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
                         choices=['Helvetica-Bold'], dest='font_name', help='font name')
        oto.add_argument('--font-size', '-fs', default='small', type=str,
                         choices=['small', 'medium', 'large'], dest='font_size',
                         help='font size')
        oto.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='text alignment')

        otm = sub_commands.add_parser('otm', help='one to one help')
        otm.add_argument('--text', '-t', type=str, default='PDFPlay', dest='text',
                         help='watermark text')
        otm.add_argument('--input', '-i', default=None, type=types.target_file_otm,
                         action=actions.target_file_otm, dest='target_file', nargs='+',
                         help='target file')
        otm.add_argument('--output', '-o', default=None,
                         type=types.output_file_otm,
                         action=actions.output_file_otm, dest='output_file',
                         help='output file')
        otm.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
                         choices=['Helvetica-Bold'], dest='font_name', help='font name')
        otm.add_argument('--font-size', '-fs', default='small', type=str,
                         choices=['small', 'medium', 'large'], dest='font_size',
                         help='font size')
        otm.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='text alignment')

        mto = sub_commands.add_parser('mto', help='one to one help')
        mto.add_argument('--text', '-t', default='PDFPlay',
                         type=types.watermark_mto,
                         action=actions.watermark_mto,
                         dest='text',
                         help='watermark text')
        mto.add_argument('--input', '-i', default=None, type=types.target_file_oto,
                         action=actions.target_file_oto, dest='target_file',
                         help='target file')
        mto.add_argument('--output', '-o', default=None,
                         type=types.output_file_otm,
                         action=actions.output_file_otm, dest='output_file',
                         help='output file')
        mto.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
                         choices=['Helvetica-Bold'], dest='font_name', help='font name')
        mto.add_argument('--font-size', '-fs', default='small', type=str,
                         choices=['small', 'medium', 'large'], dest='font_size',
                         help='font size')
        mto.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='text alignment')
        args = _update_args(parser.parse_args())
        return args
    except Exception as e:
        print(f'Error --> Bad user-input: {e}')


def _test():
    command = ['watermark', '-t', 'test target']
    args = parse_user_args(command)
    print(f'User Args: {args}')


if __name__ == '__main__':
    _test()
