#!/usr/bin/local/python3.9
# -*- coding: utf-8 -*-

"""
    Builds CLI options
"""

from argparse import ArgumentParser
from os import makedirs
from os.path import isdir
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


def _update_args(args):
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
                                description='A Python utility to manipulate PDF '
                                            'documents.',
                                epilog='''NOTE: Run --help / -h against individual 
                                commands 
                                to get more info.\nExample: pdf_play 
                                watermark -h''')
        commands = parser.add_subparsers(dest='command', help='Commands available in '
                                                              'PDF-Play. Get help: '
                                                              '"python -m pdf_play {'
                                                              'command} -h"')
        watermark = commands.add_parser('watermark', help='Watermarks PDF files.',
                                        description='Apply watermarks to PDF '
                                                    'files.')
        sub_commands = watermark.add_subparsers(dest='type', help='Types of operations '
                                                                  'for watermarking PDF '
                                                                  'files.')
        oto = sub_commands.add_parser('oto',
                                      help='One-To-One: Apply watermark text to a '
                                           'single file. Get help: "python -m pdf_play '
                                           'watermark oto -h"')
        oto.add_argument('--text', '-t', type=str, default='PDFPlay',
                         dest='text', required=True,
                         help='Watermark text, must be wrapped inside quotes if it '
                              'contains white-spaces.')
        oto.add_argument('--input', '-i', default=None, type=types.target_file_oto,
                         action=actions.target_file_oto, dest='target_file',
                         required=True,
                         help='Path to the PDF file that is to be watermarked.')
        oto.add_argument('--output', '-o', default=None, type=types.output_file_oto,
                         action=actions.output_file_oto, dest='output_file',
                         help='Name of the output file, by default '
                              '"{input-file}_watermarked.pdf" will be generated.')
        oto.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
                         choices=['Helvetica-Bold'], dest='font_name',
                         help='Name of the font that you want to use in the watermark.')
        oto.add_argument('--font-size', '-fs', default='small', type=str,
                         choices=['small', 'medium', 'large'], dest='font_size',
                         help='Size of the font.')
        oto.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='Alignment of the watermark in the document.')

        otm = sub_commands.add_parser('otm', help='One-To-Many: Apply watermark to many '
                                                  'files. Get help: "python -m pdf_play '
                                                  'watermark otm -h"')
        otm.add_argument('--text', '-t', type=str, default='PDFPlay', dest='text',
                         required=True,
                         help='Watermark text, must be wrapped inside quotes if it '
                              'contains white-spaces.')
        otm.add_argument('--input', '-i', default=None, type=types.target_file_otm,
                         action=actions.target_file_otm, dest='target_file', nargs='+',
                         required=True,
                         help='Paths to PDF files or to directories that contain PDF '
                              'files, mulitple values are allowed.')
        otm.add_argument('--output', '-o', default=None,
                         type=types.output_file_otm,
                         action=actions.output_file_otm, dest='output_file',
                         help='Path to directory where you want to save watermarked '
                              'files, by default a directory called "watermarked" will '
                              'be created in the current working directory.')
        otm.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
                         choices=['Helvetica-Bold'], dest='font_name',
                         help='Name of the font that you want to use in the watermark.')
        otm.add_argument('--font-size', '-fs', default='small', type=str,
                         choices=['small', 'medium', 'large'], dest='font_size',
                         help='Size of the font.')
        otm.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='Alignment of the watermark in the document.')

        mto = sub_commands.add_parser('mto', help='Many-To-One: Apply many different '
                                                  'watermarks to the same file. Get '
                                                  'help: "python -m pdf_play watermark '
                                                  'mto -h"')
        mto.add_argument('--text', '-t', default='PDFPlay',
                         type=types.watermark_mto,
                         action=actions.watermark_mto,
                         dest='text', nargs='+',
                         required=True,
                         help='Watermark texts or paths to a txt files that contain '
                              'watermark texts.')
        mto.add_argument('--input', '-i', default=None, type=types.target_file_oto,
                         action=actions.target_file_oto, dest='target_file',
                         required=True,
                         help='Path to the PDF file that is to be watermarked.')
        mto.add_argument('--output', '-o', default=None,
                         type=types.output_file_otm,
                         action=actions.output_file_otm, dest='output_file',
                         help='Path to directory where you want to save watermarked '
                              'files, by default a directory called "watermarked" will '
                              'be created in the current working directory.')
        mto.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
                         choices=['Helvetica-Bold'], dest='font_name',
                         help='Name of the font that you want to use in the watermark.')
        mto.add_argument('--font-size', '-fs', default='small', type=str,
                         choices=['small', 'medium', 'large'], dest='font_size',
                         help='Size of the font.')
        mto.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='Alignment of the watermark in the document.')
        args = parser.parse_args()
        return _update_args(args)
    except Exception as e:
        print(f'Error --> Bad user-input: {e}')
        raise e


def _test():
    command = ['watermark', '-t', 'test target']
    args = parse_user_args(command)
    print(f'User Args: {args}')


if __name__ == '__main__':
    _test()
