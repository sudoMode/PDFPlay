from pdf_play import __settings__ as settings
from pdf_play.core import watermark
from pdf_play.helpers import parse_user_args

args = parse_user_args()


def _watermark_mto(texts=('PDFPlay',), target_file=None, output_directory=None,
                   font_name='Helvetica-Bold',
                   font_size='medium', text_alignment='diagonal'):
    output_file = output_directory
    for text in texts:
        watermark(text, target_file, output_file=output_file, font_name=font_name,
                  font_size=font_size, text_alignment=text_alignment)


def _watermark_otm(text='PDFPlay', target_files=None, output_directory=None,
                   font_name='Helvetica-Bold',
                   font_size='medium', text_alignment='diagonal'):
    output_file = output_directory
    for file in target_files:
        watermark(text, file, output_file, font_name=font_name, font_size=font_size,
                  text_alignment=text_alignment)


def _watermark_oto(text='PDFPlay', target_file=None, output_file=None,
                   font_name='Helvetica-Bold',
                   font_size='medium', text_alignment='diagonal'):
    print('called...')
    watermark(text, target_file, output_file, font_name=font_name, font_size=font_size,
              text_alignment=text_alignment)


def _watermark():
    print('called.......')
    if not args.command == 'watermark':
        print('bad command')
        return
    type_ = args.type
    del args.command
    del args.type
    type_map = dict(oto=_watermark_oto, otm=_watermark_otm, mto=_watermark_mto)
    type_map[type_](**vars(args))


def main():
    print('Main...')
    # args = parse_user_args()
    print(f'User Args: {args}')
    if args.command == 'watermark':
        _watermark()
