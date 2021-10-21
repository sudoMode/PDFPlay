#!/usr/bin/local/python3.9
# -*- coding: utf-8 -*-

"""
    Builds CLI options
"""

from argparse import ArgumentParser

from pdf_play.__settings__ import COLORS
from pdf_play.__settings__ import FONTS
from pdf_play.__settings__ import FONT_SIZES
from pdf_play.__settings__ import VERSION
from pdf_play.helpers import _input_actions as actions
from pdf_play.helpers import _input_types as types
from pdf_play.helpers import _utils as utils

_pdf_play = f'''\n{"-" * 100}\n{"*" * 30}{" " * 16}PDF-Play{" " * 16}{"*" * 30
}\n{"-" * 100}\n'''


def parse_user_args(command=None):
    __usage = 'usage: pdf_play [-h] {watermark} ..'
    _usage = f'{_pdf_play}\n{__usage}'
    parser = ArgumentParser(prog='pdf_play',
                            description='A Python utility to watermark PDF '
                                    'documents',
                            epilog="""--> Run -h/--help against indivdual commands to 
                               get more details. Example: watermark -h""")
    parser.add_argument('-v', '--version', action='version',
                        version=f'PDF-Play: {VERSION}',
                        help='display version of the program')
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, dest='debug',
                        help='display stack trace for a failure')

    commands = parser.add_subparsers(dest='command',
                                     help="""Commands available in PDF-Play, 
                                      currently there's just one :(""")
    watermark = commands.add_parser('watermark', help='Watermarks PDF files',
                                    description='Apply watermarks to PDF '
                                            'files',
                                    epilog="""--> Run -h/--help against positional 
                                       arguments to get more details. Example: watermark 
                                       oto -h""")
    sub_commands = watermark.add_subparsers(dest='type',
                                            help="""Modes of operation for 
                                             watermarking PDF files""")
    oto = sub_commands.add_parser('oto',
                                  help="""One-To-One: Apply watermark text to a 
                                   single file""",
                                  description="""One-To-One: Use this mode when you 
                                          have got a single target file""",
                                  epilog="""--> Sample Usage: watermark oto -t 'this 
                                     is my watermark text' -i 
                                     'MyPC/Downloads/PDFFiles/sample.pdf'""")
    oto.add_argument('-t', '--text', type=str, default='PDFPlay',
                     dest='text', required=True, nargs='+',
                     action=actions.watermark_text,
                     help='(**) Text that is to be applied as the watermark')
    oto.add_argument('-i', '--input', default=None, type=types.target_file_oto,
                     action=actions.target_file_oto, dest='target_file',
                     required=True,
                     help='(**) Path to the PDF file that is to be watermarked')
    oto.add_argument('-o', '--output', default=None, type=types.output_file_oto,
                     action=actions.output_file_oto, dest='output_file',
                     help='Name of the output file, by default '
                      '"{input-file}_watermarked.pdf" will be generated')
    oto.add_argument('-fn', '--font-name', default='Helvetica-Bold', type=str,
                     choices=FONTS, dest='font_name',
                     help='Name of the font that you want to use in the watermark')
    oto.add_argument('-fs', '--font-size', default='medium', type=str,
                     choices=FONT_SIZES, dest='font_size',
                     help='Size of the font')
    oto.add_argument('-fc', '--font-color', default='lightred', type=str,
                     choices=COLORS, dest='font_color',
                     help='Color of the font')
    oto.add_argument('-ta', '--text-alignment', default='diagonal', type=str,
                     choices=['horizontal', 'diagonal'], dest='text_alignment',
                     help='Alignment of the watermark in the document')
    oto.add_argument('-p', '--print', action='store_true',
                     default=False, dest='verbose',
                     help='Display informational messages')

    otm = sub_commands.add_parser('otm', help='One-To-Many: Apply watermark to '
                                          'multiple files',
                                  description='One-To-Many: Use this mode when you '
                                          'have got multiple target/S files',
                                  epilog=""""--> Sample Usage: watermark otm -t 'this 
                                     is my watermark text' -i 'sample1.pdf' 'sample2.pdf' 
                                     'MyPC/Downloads/PDFFiles'""")
    otm.add_argument('-t', '--text', type=str, default='PDFPlay', dest='text',
                     required=True, action=actions.watermark_text, nargs='+',
                     help='(**) Text that is to be applied as the watermark')
    otm.add_argument('-i', '--input', default=None, type=types.target_file_otm,
                     action=actions.target_file_otm, dest='target_files', nargs='+',
                     required=True,
                     help="""(**) Paths to files/directories that contain
                      your target files""")
    otm.add_argument('-o', '--output', default=None,
                     type=types.output_file_otm,
                     action=actions.output_file_otm, dest='output_directory',
                     help='Directory to save watermarked files')
    otm.add_argument('-fn', '--font-name', default='Helvetica-Bold', type=str,
                     choices=FONTS, dest='font_name',
                     help='Name of the font that you want to use in the watermark')
    otm.add_argument('-fs', '--font-size', default='medium', type=str,
                     choices=FONT_SIZES, dest='font_size',
                     help='Size of the font')
    otm.add_argument('-fc', '--font-color', default='lightred', type=str,
                     choices=COLORS, dest='font_color',
                     help='Color of the font')
    otm.add_argument('-ta', '--text-alignment', default='diagonal', type=str,
                     choices=['horizontal', 'diagonal'], dest='text_alignment',
                     help='Alignment of the watermark in the document')
    otm.add_argument('-p', '--print', action='store_true',
                     default=False, dest='verbose',
                     help='Display informational messages')

    mto = sub_commands.add_parser('mto', help='Many-To-One: Apply many different '
                                          'watermarks to a single file',
                                  description="""Many-To-One: Use this mode when you
                                          want to watermark a file multiple times with
                                          different watermark texts""",
                                  epilog="""--> Sample usage: watermark mto -t 
                                     'watermark text#1' 'watermark text#2' 
                                     'MyPC/SampleWatermarks/sample1.txt' -i 'sample.pdf'
                                     """)
    mto.add_argument('-t', '--text', default=None,
                     type=str,
                     action=actions.watermark_mto,
                     dest='texts', nargs='+',
                     help="""Texts to watermark, accepts multiple values 
                      separated by white-space. Ex: 'watermark #1' 'watermark #2'""")
    mto.add_argument('-tf', '--text-file', default=None,
                     type=types.watermark_mto_file,
                     action=actions.watermark_mto_file,
                     dest='text_data',
                     help="""Path to the CSV/Excel file containing watermark 
                      texts.
                      """)
    mto.add_argument('-nh', '--name-header', default=None,
                     type=str,
                     dest='name_header',
                     help="""Name of the column to be used for file names""")
    mto.add_argument('-th', '--text-header', default=None,
                     type=str,
                     dest='text_header',
                     help="""Name of the column to be used for watermark texts""")
    mto.add_argument('-hr', '--header-row', default=1,
                     type=int,
                     dest='header_row',
                     help="""Index of the header row""")
    mto.add_argument('-i', '--input', default=None, type=types.target_file_mto,
                     action=actions.target_file_oto, dest='target_file',
                     required=True,
                     help='(**) Path to the PDF file that is to be watermarked')
    mto.add_argument('-o', '--output', default=None,
                     type=types.output_file_otm,
                     action=actions.output_file_otm, dest='output_directory',
                     help='Directory to save watermarked files')
    mto.add_argument('-fn', '--font-name', default='Helvetica-Bold', type=str,
                     choices=FONTS, dest='font_name',
                     help='Name of the font that you want to use in the watermark')
    mto.add_argument('-fs', '--font-size', default='medium', type=str,
                     choices=FONT_SIZES, dest='font_size',
                     help='Size of the font')
    mto.add_argument('-fc', '--font-color', default='lightred', type=str,
                     choices=COLORS, dest='font_color',
                     help='Color of the font')
    mto.add_argument('-rgb', '--red-green-blue', default=(0, 0, 0), type=int,
                     nargs='+',
                     dest='rgb',
                     help='RGB values, between 0-255. Ex: -rgb 255 255 255')
    mto.add_argument('-tr', '--tranparency', default=0, type=int,
                     choices=range(0, 101, 10),
                     dest='tranparency',
                     help='Tranparency percentage')
    alignment_choices = ['horizontal', 'diagonal']
    alignment_choices.extend(list(range(0, 361, 90)))
    mto.add_argument('-ta', '--text-alignment', default='diagonal', type=str,
                     choices=alignment_choices, dest='text_alignment',
                     help='Alignment of the watermark in the document')
    mto.add_argument('-p', '--print', action='store_true',
                     default=False, dest='verbose',
                     help='Display informational messages')
    args = parser.parse_args() if command is None else parser.parse_args(command)
    utils.validate_args(parser, args)
    args = utils.update_args(args)
    return args


def parse_watermark_args():
    try:
        parser = ArgumentParser(prog='watermark',
                                description='A Python utility to watermark PDF '
                                            'documents',
                                epilog="""--> Run -h/--help against positional 
                                        arguments to get more details. Example: watermark 
                                        oto -h""")
        sub_commands = parser.add_subparsers(dest='type',
                                             help="""Modes of operation for 
                                                 watermarking PDF files""")
        oto = sub_commands.add_parser('oto',
                                      help="""One-To-One: Apply watermark text to a 
                                                   single file""",
                                      description="""One-To-One: Use this mode when you 
                                              have got a single target file""",
                                      epilog="""--> Sample Usage: watermark oto -t 'this 
                                              is my watermark text' -i 
                                              'MyPC/Downloads/PDFFiles/sample.pdf'""")
        oto.add_argument('-t', '--text', type=str, default='PDFPlay',
                         dest='text', required=True, nargs='+',
                         action=actions.watermark_text,
                         help='(**) Text that is to be applied as the watermark')
        oto.add_argument('-i', '--input', default=None, type=types.target_file_oto,
                         action=actions.target_file_oto, dest='target_file',
                         required=True,
                         help='(**) Path to the PDF file that is to be '
                              'watermarked')
        oto.add_argument('-o', '--output', default=None, type=types.output_file_oto,
                         action=actions.output_file_oto, dest='output_file',
                         help='Name of the output file, by default '
                              '"{input-file}_watermarked.pdf" will be generated')
        oto.add_argument('-fn', '--font-name', default='Helvetica-Bold', type=str,
                         choices=FONTS, dest='font_name',
                         help='Name of the font that you want to use in the watermark')
        oto.add_argument('-fs', '--font-size', default='medium', type=str,
                         choices=FONT_SIZES, dest='font_size',
                         help='Size of the font')
        oto.add_argument('-fc', '--font-color', default='lightred', type=str,
                         choices=COLORS, dest='font_color',
                         help='Color of the font')
        oto.add_argument('-ta', '--text-alignment', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='Alignment of the watermark in the document')
        oto.add_argument('-p', '--print', action='store_true',
                         default=False, dest='verbose',
                         help='Display informational messages')

        otm = sub_commands.add_parser('otm', help='One-To-Many: Apply watermark to '
                                                  'multiple files',
                                      description='One-To-Many: Use this mode when you '
                                                  'have got multiple target/S files',
                                      epilog=""""--> Sample Usage: watermark otm -t 'this 
                                              is my watermark text' -i 'sample1.pdf' 'sample2.pdf' 
                                              'MyPC/Downloads/PDFFiles'""")
        otm.add_argument('-t', '--text', type=str, default='PDFPlay', dest='text',
                         required=True, action=actions.watermark_text, nargs='+',
                         help='(**) Text that is to be applied as the watermark')
        otm.add_argument('-i', '--input', default=None, type=types.target_file_otm,
                         action=actions.target_file_otm, dest='target_files', nargs='+',
                         required=True,
                         help="""(**) Paths to files/directories that contain
                                 your target files""")
        otm.add_argument('-o', '--output', default=None,
                         type=types.output_file_otm,
                         action=actions.output_file_otm, dest='output_directory',
                         help='Directory to save watermarked files')
        otm.add_argument('-fn', '--font-name', default='Helvetica-Bold', type=str,
                         choices=FONTS, dest='font_name',
                         help='Name of the font that you want to use in the watermark')
        otm.add_argument('-fs', '--font-size', default='medium', type=str,
                         choices=FONT_SIZES, dest='font_size',
                         help='Size of the font')
        otm.add_argument('-fc', '--font-color', default='lightred', type=str,
                         choices=COLORS, dest='font_color',
                         help='Color of the font')
        otm.add_argument('-ta', '--text-alignment', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='Alignment of the watermark in the document')
        otm.add_argument('-p', '--print', action='store_true',
                         default=False, dest='verbose',
                         help='Display informational messages')

        mto = sub_commands.add_parser('mto', help='Many-To-One: Apply many different '
                                                  'watermarks to a single file',
                                      description="""Many-To-One: Use this mode when you
                                              want to watermark a file multiple times with
                                              different watermark texts""",
                                      epilog="""--> Sample usage: watermark mto -t 
                                              'watermark text#1' 'watermark text#2' 
                                              'MyPC/SampleWatermarks/sample1.txt' -i 
                                              'sample.pdf'""")
        mto.add_argument('-t', '--text', default='PDFPlay',
                         type=types.watermark_mto,
                         action=actions.watermark_mto,
                         dest='texts', nargs='+',
                         help="""(**) Texts that are to be watermarked or path to 
                         csv/excel files that contain watermark text. These file can 
                         contain upto 2 columns, first for output file name and second 
                         for the watermark text, if there's just one column then it 
                         will be used as watermark text.""")
        mto.add_argument('-i', '--input', default=None, type=types.target_file_mto,
                         action=actions.target_file_oto, dest='target_file',
                         required=True,
                         help='(**) Path to the PDF file that is to be watermarked')
        mto.add_argument('-o', '--output', default=None,
                         type=types.output_file_otm,
                         action=actions.output_file_otm, dest='output_directory',
                         help='Directory to save watermarked files')
        mto.add_argument('-fn', '--font-name', default='Helvetica-Bold', type=str,
                         choices=FONTS, dest='font_name',
                         help='Name of the font that you want to use in the watermark')
        mto.add_argument('-fs', '--font-size', default='medium', type=str,
                         choices=FONT_SIZES, dest='font_size',
                         help='Size of the font')
        mto.add_argument('-fc', '--font-color', default='lightred', type=str,
                         choices=COLORS, dest='font_color',
                         help='Color of the font')
        mto.add_argument('-ta', '--text-alignment', default='diagonal', type=str,
                         choices=['horizontal', 'diagonal'], dest='text_alignment',
                         help='Alignment of the watermark in the document')
        mto.add_argument('-p', '--print', action='store_true',
                         default=False, dest='verbose',
                         help='Display informational messages')

        args = parser.parse_args()
        args.command = 'watermark'
        # _validate_args(parser, args)
        # args = _update_args(args)
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
