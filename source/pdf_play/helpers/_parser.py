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

_pdf_play = f'''\n{"-" * 100}\n{"*" * 30}{" " * 16}PDF-Play{" " * 16}{"*" * 30
}\n{"-" * 100}\n'''


def _validate_otm(args):
    if args.output_directory is None:
        args.output_directory = 'watermarked'
        if not isdir(args.output_directory):
            print('User did not provide an output location, a directory called '
                  '"watermarked" will be created to store all the watermarked PDF(s).')
            makedirs(args.output_directory)


def _validate_mto(args):
    _validate_otm(args)


def _validate_oto(args):
    if args.output_file is None:
        # print('--> User did not provide an output file, a watermarked copy of the input '
        #       'file will be created.')
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


def _validate_args(parser, args):
    if args.command is None:
        print(_pdf_play)
        parser.print_help()
        exit(0)
    else:
        if args.type is None:
            print('\n--> User must specify the mode of operation when trying to '
                  f'watermark PDF files. Get help: "python -m pdf_play  {args.command} '
                  '-h".''')
            exit(0)


def parse_user_args(command=None):
    __usage = 'usage: pdf_play [-h] {watermark} ...'
    _usage = f'{_pdf_play}\n{__usage}'
    try:
        parser = ArgumentParser(prog='pdf_play',
                                description='A Python utility to watermark PDF '
                                            'documents.',
                                epilog='''--> Run -h/--help against indivdual commands to 
                                get more details. Example: "python -m pdf_play watermark 
                                -h"''')
        commands = parser.add_subparsers(dest='command',
                                         help='''Commands available in PDF-Play, 
                                         currently there's just one :(''')
        watermark = commands.add_parser('watermark', help='Watermarks PDF files.',
                                        description='Apply watermarks to PDF '
                                                    'files.',
                                        epilog='''--> Sample usage: python -m pdf_play 
                                        watermark oto -h''')
        sub_commands = watermark.add_subparsers(dest='type',
                                                help='''Modes of operation for 
                                                     watermarking PDF files.''')
        oto = sub_commands.add_parser('oto',
                                      help='''One-To-One: Apply watermark text to a 
                                           single file.''',
                                      description='''One-To-One: Use this mode when you 
                                      have got a single target file.''',
                                      epilog='''--> Sample Usage: python -m pdf_play 
                                             watermark oto -t this is my watermark 
                                             text -i sample.pdf''')
        oto.add_argument('--text', '-t', type=str, default='PDFPlay',
                         dest='text', required=True, nargs='+',
                         action=actions.watermark_text,
                         help='(**) Text that is to be applied as the watermark.')
        oto.add_argument('--input', '-i', default=None, type=types.target_file_oto,
                         action=actions.target_file_oto, dest='target_file',
                         required=True,
                         help='(**) Path to the PDF file that is to be watermarked.')
        oto.add_argument('--output', '-o', default=None, type=types.output_file_oto,
                         action=actions.output_file_oto, dest='output_file',
                         help='Name of the output file, by default '
                              '"{input-file}_watermarked.pdf" will be generated.')
        oto.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
                         choices=['Helvetica-Bold'], dest='font_name',
                         help='Name of the font that you want to use in the watermark.')
        oto.add_argument('--font-size', '-fs', default='medium', type=str,
                         choices=['small', 'medium', 'large'], dest='font_size',
                         help='Size of the font.')
        oto.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='Alignment of the watermark in the document.')

        otm = sub_commands.add_parser('otm', help='One-To-Many: Apply watermark to '
                                                  'multiple files.',
                                      description='One-To-Many: Use this mode when you '
                                                  'have got multiple target files.',
                                      epilog='''--> Sample Usage: python -m pdf_play
                                             watermark otm -t this is my watermark
                                             text -i sample1.pdf sample2.pdf
                                             MyPC/Downloads/PDFFiles ''')
        otm.add_argument('--text', '-t', type=str, default='PDFPlay', dest='text',
                         required=True, action=actions.watermark_text, nargs='+',
                         help='(**) Text that is to be applied as the watermark.')
        otm.add_argument('--input', '-i', default=None, type=types.target_file_otm,
                         action=actions.target_file_otm, dest='target_files', nargs='+',
                         required=True,
                         help='''(**) Paths to files/directories that contain
                         your target files.''')
        otm.add_argument('--output', '-o', default=None,
                         type=types.output_file_otm,
                         action=actions.output_file_otm, dest='output_directory',
                         help='Directory to save watermarked files.')
        otm.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
                         choices=['Helvetica-Bold'], dest='font_name',
                         help='Name of the font that you want to use in the watermark.')
        otm.add_argument('--font-size', '-fs', default='medium', type=str,
                         choices=['small', 'medium', 'large'], dest='font_size',
                         help='Size of the font.')
        otm.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='Alignment of the watermark in the document.')
        #
        # mto = sub_commands.add_parser('mto', help='Many-To-One: Apply many different '
        #                                           'watermarks to a single file',
        #                               description='''Many-To-One: Use this mode when you
        #                               want to watermark a file multiple times with
        #                               different watermark texts.''',
        #                               epilog='''--> Sample usage: python -m pdf_play
        #                               watermark mto -t watermark text#1, watermark
        #                               text#2, MyPC/SampleWatermarks/sample1.txt -i
        #                               sample.pdf''')
        # mto.add_argument('--text', '-t', default='PDFPlay',
        #                  type=types.watermark_mto,
        #                  action=actions.watermark_mto,
        #                  dest='texts',
        #                  help='''(**) Texts that are to be watermarked or path to a txt
        #                       file that contains such texts.
        #                       (Expected comma separated values)''')
        # mto.add_argument('--input', '-i', default=None, type=types.target_file_oto,
        #                  action=actions.target_file_oto, dest='target_file',
        #                  required=True,
        #                  help='(**) Path to the PDF file that is to be watermarked.')
        # mto.add_argument('--output', '-o', default=None,
        #                  type=types.output_file_otm,
        #                  action=actions.output_file_otm, dest='output_directory',
        #                  help='''Directory to save watermarked files.''')
        # mto.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
        #                  choices=['Helvetica-Bold'], dest='font_name',
        #                  help='Name of the font that you want to use in the watermark.')
        # mto.add_argument('--font-size', '-fs', default='medium', type=str,
        #                  choices=['small', 'medium', 'large'], dest='font_size',
        #                  help='Size of the font.')
        # mto.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
        #                  choices=['horizontal', 'diagonal'], dest='text_alignment',
        #                  help='Alignment of the watermark in the document.')

        args = parser.parse_args() if command is None else parser.parse_args(command)
        _validate_args(parser, args)
        args = _update_args(args)
        return args
    except Exception as e:
        print(f'Error --> Bad user-input: {e}')
        raise e


def parse_watermark_args():
    try:
        parser = ArgumentParser(prog='watermark',
                                description='A Python utility to watermark PDF '
                                            'documents.',
                                epilog='''--> Run -h/--help to get more details. 
                                Example: "watermark -h"''')
        commands = parser.add_subparsers(dest='type',
                                         help='''Modes of operation for 
                                                 watermarking PDF files.''')
        oto = commands.add_parser('oto',
                                  help='''One-To-One: Apply watermark text to a 
                                                   single file.''',
                                  description='''One-To-One: Use this mode when you 
                                              have got a single target file.''',
                                  epilog='''--> Sample Usage: python -m pdf_play 
                                                     watermark oto -t this is my watermark 
                                                     text -i sample.pdf''')
        oto.add_argument('--text', '-t', type=str, default='PDFPlay',
                         dest='text', required=True, nargs='+',
                         action=actions.watermark_text,
                         help='(**) Text that is to be applied as the watermark.')
        oto.add_argument('--input', '-i', default=None, type=types.target_file_oto,
                         action=actions.target_file_oto, dest='target_file',
                         required=True,
                         help='(**) Path to the PDF file that is to be watermarked.')
        oto.add_argument('--output', '-o', default=None, type=types.output_file_oto,
                         action=actions.output_file_oto, dest='output_file',
                         help='Name of the output file, by default '
                              '"{input-file}_watermarked.pdf" will be generated.')
        oto.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
                         choices=['Helvetica-Bold'], dest='font_name',
                         help='Name of the font that you want to use in the watermark.')
        oto.add_argument('--font-size', '-fs', default='medium', type=str,
                         choices=['small', 'medium', 'large'], dest='font_size',
                         help='Size of the font.')
        oto.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='Alignment of the watermark in the document.')

        otm = commands.add_parser('otm',
                                  help='One-To-Many: Apply watermark to multiple files.',
                                  description='One-To-Many: Use this mode when you '
                                              'have got multiple target files.',
                                  epilog='''--> Sample Usage: python -m pdf_play
                                             watermark otm -t this is my watermark
                                             text -i sample1.pdf sample2.pdf
                                             MyPC/Downloads/PDFFiles ''')
        otm.add_argument('--text', '-t', type=str, default='PDFPlay', dest='text',
                         required=True, action=actions.watermark_text, nargs='+',
                         help='(**) Text that is to be applied as the watermark.')
        otm.add_argument('--input', '-i', default=None, type=types.target_file_otm,
                         action=actions.target_file_otm, dest='target_files', nargs='+',
                         required=True,
                         help='''(**) Paths to files/directories that contain
                         your target files.''')
        otm.add_argument('--output', '-o', default=None,
                         type=types.output_file_otm,
                         action=actions.output_file_otm, dest='output_directory',
                         help='Directory to save watermarked files.')
        otm.add_argument('--font-name', '-fn', default='Helvetica-Bold', type=str,
                         choices=['Helvetica-Bold'], dest='font_name',
                         help='Name of the font that you want to use in the watermark.')
        otm.add_argument('--font-size', '-fs', default='medium', type=str,
                         choices=['small', 'medium', 'large'], dest='font_size',
                         help='Size of the font.')
        otm.add_argument('--text-alignment', '-ta', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='Alignment of the watermark in the document.')

        args = parser.parse_args()
        args.command = 'watermark'
        _validate_args(parser, args)
        args = _update_args(args)
        return args
    except Exception as e:
        print(f'Error --> Bad user-input: {e}')
        raise e


def _test():
    command = ['watermark', '-t', 'test target']
    args = parse_user_args(command)
    print(f'User Args: {args}')


if __name__ == '__main__':
    _test()
