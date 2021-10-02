from pdf_play import __settings__ as settings
from pdf_play.core import watermark
from pdf_play.helpers import parse_user_args

command = ['watermark', '-t', 'dummy watermark text!', '-tf', f'{settings.INPUT_FILE}']
args = parse_user_args(command)
# TODO: temporary

command = args.command
del args.command


def main():
    # print(f'User Args: {args}')
    if command == 'watermark':
        watermark(**vars(args))


if __name__ == '__main__':
    main()
