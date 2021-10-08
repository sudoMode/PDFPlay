from pdf_play import __settings__ as settings
from pdf_play.core import watermark
from pdf_play.helpers import parse_user_args


def main():
    args = parse_user_args()
    # args.target_file = settings.INPUT_FILE
    print(f'User Args: {args}')
    # _command = args.command
    # del args.command
    # if _command == 'watermark':
    #     watermark(**vars(args))
