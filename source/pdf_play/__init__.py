from os.path import join
from os.path import sep
from pathlib import Path
from pdf_play import __settings__ as settings
from pdf_play.core import watermark
from pdf_play.helpers import parse_user_args
from pdf_play.helpers import parse_watermark_args


def _watermark_mto(texts=('PDFPlay',), target_file=None, output_directory=None,
                   font_name='Helvetica-Bold',
                   font_size='medium', text_alignment='diagonal'):
    raise NotImplementedError('To be implemented...')


def _watermark_otm(text='PDFPlay', target_files=None, output_directory=None,
                   font_name='Helvetica-Bold',
                   font_size='medium', text_alignment='diagonal'):
    for target_file in target_files:
        name_and_extension = target_file.split(sep)[-1]
        name, extension = name_and_extension.split('.')
        output_file = join(output_directory, f'{name}_watermarked.{extension}')
        watermark(text, target_file, output_file, font_name=font_name,
                  font_size=font_size, text_alignment=text_alignment)


def _watermark_oto(text='PDFPlay', target_file=None, output_file=None,
                   font_name='Helvetica-Bold',
                   font_size='medium', text_alignment='diagonal'):
    watermark(text, target_file, output_file, font_name=font_name, font_size=font_size,
              text_alignment=text_alignment)


def _watermark(args=None):
    if args is None:
        args = parse_watermark_args()
    type_ = args.type
    del args.type
    del args.command
    type_map = dict(oto=_watermark_oto, otm=_watermark_otm)
    type_map[type_](**vars(args))


def main():
    args = parse_user_args()
    command_map = dict(watermark=_watermark)
    command_map[args.command](args)
