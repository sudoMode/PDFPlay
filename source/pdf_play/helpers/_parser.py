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
from os.path import join
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


def _validate_mto(args):
    _validate_otm(args)


def _validate_oto(args):
    if args.output_file is None:
        print('User did not provide an output file, a watermarked copy of the input '
              'file will be created')
        base = Path(args.target_file).parent.resolve()
        file_name = args.target_file.split(sep)[-1]
        name, extension = file_name.split('.')
        args.output_file = join(base, f'{name}_watermarked.{extension}')


def _update_args(parser):
    args = parser.parse_args()
    print(f'UA: {args}')
    if args.command is None:
        print(parser.print_help())
        exit(0)
    if args.type == 'oto':
        _validate_oto(args)
    if args.type == 'otm':
        _validate_otm(args)
    if args.type == 'mto':
        _validate_mto(args)
    return args


def parse_user_args(command=None):
    try:
        parser = ArgumentParser(prog='pdf_play',
                                description='A Python utility to manipulate PDF files.')
        commands = parser.add_subparsers(dest='command')
        watermark = commands.add_parser('watermark', help='Watermarks PDF files.',
                                        description='Watermark PDF files.')
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
        return _update_args(parser)
    except Exception as e:
        print(f'Error --> Bad user-input: {e}')
        raise e


def _test():
    command = ['watermark', '-t', 'test target']
    args = parse_user_args(command)
    print(f'User Args: {args}')


if __name__ == '__main__':
    _test()
