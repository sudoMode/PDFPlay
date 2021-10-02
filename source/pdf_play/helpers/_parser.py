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

_TEXT = dict(name='--text', flag='-t', type=str, default='',
             dest='text', help='Watermark text.')

_TARGET_FILE = dict(name='--target-file', flag='-tf', type=str, default=None,
                    dest='target_file', help='Target PDF(s).')

_OUTPUT_FILE = dict(name='--output-file', flag='-of', type=str, default=None,
                    dest='output_file', help='Output PDF(s).')

_FONT_NAME = dict(name='--font-name', flag='-fn', type=str, default='Helvetica',
                  dest='font_name', help='Name of the font.')

_FONT_SIZE = dict(name='--font-size', flag='-fs', type=int, default=25,
                  dest='font_size', help='Size of the font.')

_ROTATION = dict(name='--rotation-angle', flag='-ra', type=int, default=0,
                 dest='rotation', help='Degree of rotation.')

_POSITION_X = dict(name='--position-x', flag='-px', type=int, default=0,
                   dest='position_x', help='Postion on X-axis.')

_POSITION_Y = dict(name='--position-y', flag='-py', type=int, default=0,
                   dest='position_y', help='Postion on Y-axis.')

_COLOR = dict(name='--color', flag='-c', type=str, default='black',
              dest='color', help='Color of the text.')

_TRANSPARENCY = dict(name='--transparency', flag='-tp', type=int, default=0,
                     choices=range(1, 101), dest='transparency',
                     help='Opacity of the text.')

_PAGE_SIZE = dict(name='--page-size', flag='-ps', type=str, default='A4',
                  dest='page_size', help='Size of the page.')

_OPTIONAL_ARGUMENTS = dict(text=_TEXT, target_file=_TARGET_FILE,
                           output_file=_OUTPUT_FILE, font_name=_FONT_NAME,
                           font_size=_FONT_SIZE, rotation=_ROTATION,
                           position_x=_POSITION_X, position_y=_POSITION_Y,
                           color=_COLOR, transparency=_TRANSPARENCY, page_size=_PAGE_SIZE)
_POSITIONAL_ARGUMENTS = None
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


def parse_user_args(command):
    parser = ArgumentParser(prog='pdf_play',
                            description='Play with your PDF documents!'
                            )

    sub_parser = parser.add_subparsers(dest='command')
    for name, config in _CLI.items():
        _build_command(sub_parser, name=name, **config)

    return parser.parse_args(command)


def _test():
    command = ['watermark', '-t', 'test target']
    args = parse_user_args(command)
    print(f'User Args: {args}')


if __name__ == '__main__':
    _test()
