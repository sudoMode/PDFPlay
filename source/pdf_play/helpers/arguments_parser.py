from argparse import ArgumentParser

_FONT_NAME = dict(name='--font-name', flag='-fn', type=str, default='xyz',
                  dest='font_name', help='Font to be used for watermark text.')

# build commands
# watermark
_OPTIONAL_ARGUMENTS = dict(font_name=_FONT_NAME)
_POSITIONAL_ARGUMENTS = {}
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


def parse_user_args():
    parser = ArgumentParser(prog='pdf_play',
                            description='Play with your PDF documents!',
                            )

    sub_parser = parser.add_subparsers()
    for name, config in _CLI.items():
        _build_command(sub_parser, name=name, **config)

    return parser.parse_args()


def _test():
    args = parse_user_args()
    print(f'User Args: {args}')


if __name__ == '__main__':
    _test()
