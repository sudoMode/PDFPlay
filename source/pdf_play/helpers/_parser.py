#!/usr/bin/local/python3.9
# -*- coding: utf-8 -*-

"""
    Builds CLI options
    NOTE: call from terminal
"""

from argparse import ArgumentParser

# TODO: make more user-friendly options

# build commands
# watermark


# optional arguments built specifically for tickers command, do not alter these
_LIST = dict(name='--list', flag='-l', type=str, nargs='+', dest='tickers', default=None,
             action=None, help='Accepts multiple ticker IDs separated by white space.')

_FILE = dict(name='--file', flag='-fp', type=str, dest='tickers', action=None,
             help='Accepts a file path that contains ticker IDs, '
                  'only CSV file are supported that must have a column called "ecode". '
                  '(Supports relative paths.)')

_URL = dict(name='--url', flag='-u', type=str, dest='tickers',
            action=None,
            help='Accepts a URL to Google Sheets containing ticker IDs')

# use above mentioned options, to build a config for user-facing commands
# build config for tickers command
_OPTIONAL_ARGUMENTS = dict(list=_LIST, file=_FILE, url=_URL)
_POSITIONAL_ARGUMENTS = None
_TICKERS = dict(help='Pass custom ticker ID(s) as an input to the program.',
                optional_arguments=_OPTIONAL_ARGUMENTS,
                positional_arguments=_POSITIONAL_ARGUMENTS)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# optional arguments built specifically for tickers command, do not alter these
_I1 = dict(name='--I1', flag='-i1', type=str, nargs='+', dest='tickers', default=None,
           action=None, help='Accepts multiple ticker IDs separated by white space.')

_I2 = dict(name='--I2', flag='-i1', type=str, dest='tickers', action=None,
           help='Accepts a file path that contains ticker IDs')

_I3 = dict(name='--I3', flag='-i3', type=str, dest='tickers',
           action=None, help='Accepts a URL to Google Sheets containing ticker IDs')

# use above mentioned options, to build a config for user-facing commands
# build config for tickers command
_OPTIONAL_ARGUMENTS = dict(i1=_I1, i2=_I2, i3=_I3)
_POSITIONAL_ARGUMENTS = None
_STYLE = dict(help='Pass custom ticker ID(s) as an input to the program.',
              optional_arguments=_OPTIONAL_ARGUMENTS,
              positional_arguments=_POSITIONAL_ARGUMENTS)


_TEXT = dict(name='--text', flag='-t', type=str, default='PDFPlay',
             dest='text', help='Watermark text.')

_TARGET_FILE = dict(name='--target-file', flag='-tf', type=str, default=None,
                    dest='target_file', help='Target PDF(s).')

_OUTPUT_FILE = dict(name='--output-file', flag='-of', type=str, default=None,
                    dest='output_file', help='Output PDF(s).')

_FONT_NAME = dict(name='--font-name', flag='-fn', type=str, default='Helvetica-Bold',
                  dest='font_name', help='Name of the font.')

_FONT_SIZE = dict(name='--font-size', flag='-fs', type=str, default='medium',
                  choices=['small', 'medium', 'large'],
                  dest='font_size', help='Size of the font.')

_ROTATION = dict(name='--rotation-angle', flag='-ra', type=int, default=0,
                 dest='rotation', help='Degree of rotation.')

_POSITION_X = dict(name='--position-x', flag='-px', type=str, default='center',
                   choices=['left', 'right', 'center'], dest='position_x',
                   help='Postion on X-axis.')

_POSITION_Y = dict(name='--position-y', flag='-py', type=str, default='center',
                   choices=['bottom', 'top', 'center'],
                   dest='position_y', help='Postion of the watermark.')

_TEXT_ALIGNMENT = dict(name='--text-alignment', flag='-ta', type=str, default='diagonal',
                       choices=['horizontal', 'vertical', 'diagonal'],
                       dest='text_alignment', help='Text alignment.')

_COLOR = dict(name='--color', flag='-c', type=str, default='black',
              dest='color', help='Color of the text.')

_TRANSPARENCY = dict(name='--transparency', flag='-tp', type=int, default=0,
                     choices=range(0, 101, 10), dest='transparency',
                     help='Opacity of the text.')

_PAGE_SIZE = dict(name='--page-size', flag='-ps', type=str, default=None,
                  dest='page_size', help='Size of the page.')

_OPTIONAL_ARGUMENTS = dict(text=_TEXT, target_file=_TARGET_FILE,
                           output_file=_OUTPUT_FILE, font_name=_FONT_NAME,
                           font_size=_FONT_SIZE,
                           position_x=_POSITION_X, position_y=_POSITION_Y,
                           color=_COLOR,
                           page_size=_PAGE_SIZE, text_alignment=_TEXT_ALIGNMENT)
_POSITIONAL_ARGUMENTS = dict(tickers=_TICKERS, style=_STYLE)
_WATERMARK = dict(help='Watermark PDF documents!',
                  description='Allows the user to watermark multiple documents at once.',
                  optional_arguments=_OPTIONAL_ARGUMENTS,
                  positional_arguments=_POSITIONAL_ARGUMENTS)

_CLI = dict(watermark=_WATERMARK)


def _add_positional_arguments(parser, config):
    if not (isinstance(parser, ArgumentParser)):
        raise TypeError(f'Expected "ArgumentParser" object, received {type(parser)}')
    for name, options in config.items():
        sub_parser = parser.add_subparsers(dest=name)
        _build_command(sub_parser, name=name, **options)


def _add_optional_arguments(parser, config):
    if not (isinstance(parser, ArgumentParser)):
        raise TypeError(f'Expected "ArgumentParser" object, received {type(parser)}')
    for _, options in config.items():
        name, flag = options['name'], options['flag']
        options = {k: v for (k, v) in options.items() if k not in ['name', 'flag']}
        parser.add_argument(name, flag, **options)


# noinspection PyShadowingBuiltins
def _build_command(sub_parser, name=None, help=None, description=None,
                   positional_arguments=None, optional_arguments=None):
    if sub_parser is None:
        raise TypeError(f'Expected "argparse._SubParserAction" object, received "None".')
    command = sub_parser.add_parser(name, help=help, description=description)
    if optional_arguments is not None:
        _add_optional_arguments(command, optional_arguments)
    if positional_arguments is not None:
        _add_positional_arguments(command, positional_arguments)


def parse_user_args(command=None):
    parser = ArgumentParser(prog='pdf_play', description='Play with your PDF documents!')
    sub1 = parser.add_subparsers(dest='command')
    watermark = sub1.add_parser('watermark', help='WM help!', description='WM des!')
    # watermark.add_argument('--one', '-1', help='one help')
    sub2 = watermark.add_subparsers(dest='style')
    style = sub2.add_parser('style', help='style help!', description='style des!')
    style.add_argument('--font-name', '-fn', help='one help', dest='font_name')

    # for name, config in _CLI.items():
    #     _build_command(sub_parser, name=name, **config)
    #
    return parser.parse_args(command)


def _test():
    command = ['watermark', '-t', 'test target']
    args = parse_user_args(command)
    print(f'User Args: {args}')


if __name__ == '__main__':
    _test()
