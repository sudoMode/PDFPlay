from pdf_play import __settings__ as settings
from pdf_play.core import watermark
from pdf_play.helpers import parse_user_args


def main():
    print('Called  main...')
    args = parse_user_args()
    # args.target_file = settings.INPUT_FILE
    print(f'User Args: {args}')
    # _command = args.command
    # del args.command
    # if _command == 'watermark':
    #     watermark(**vars(args))


def _test():
    command = ['watermark',
               '-t', 'singh.mandeep2207@gmail.com',
               '-tf', settings.INPUT_FILE2,
               '-fs', 'large',
               '-ta', 'diagonal',
               '-px', 'center',
               '-py', 'center',
               '-fn', 'Helvetica-Bold']
    args = parse_user_args(command)
    print(f'User Args: {args}')
    return
    # _command = args.command
    # del args.command
    # if _command == 'watermark':
    #     watermark(**vars(args))


if __name__ == '__main__':
    _test()
