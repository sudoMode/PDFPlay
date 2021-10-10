from os.path import join
from os.path import sep

from pdf_play import __settings__ as settings
from pdf_play.core import watermark
from pdf_play.helpers import parse_user_args
from pdf_play.helpers import parse_watermark_args


def _watermark_mto(texts=('PDFPlay',), target_file=None, output_directory=None,
                   font_name='Helvetica-Bold', font_size='medium',
                   font_color='lightred', text_alignment='diagonal', verbose=False):
    total = len(texts)
    if verbose:
        print(f'--> Received {total} watermark texts...')
    for i, text in enumerate(texts):
        output_file = join(output_directory, f'{text}.pdf')
        watermark(text, target_file, output_file, font_name=font_name,
                  font_size=font_size, font_color=font_color,
                  text_alignment=text_alignment)
        if verbose:
            print(f'--> Watermarked: {i + 1} / {total}', end='\r')
    if verbose:
        print(f'--> Success! Find watermarked files in a directpry called:'
              f' {output_directory}')


def _watermark_otm(text='PDFPlay', target_files=None, output_directory=None,
                   font_name='Helvetica-Bold', font_size='medium',
                   font_color='lightred', text_alignment='diagonal', verbose=False):
    total = len(target_files)
    if verbose:
        print(f'--> Received {total} target files...')
    for i, target_file in enumerate(target_files):
        name_and_extension = target_file.split(sep)[-1]
        name, extension = name_and_extension.split('.')
        output_file = join(output_directory, f'{name}_watermarked.{extension}')
        watermark(text, target_file, output_file, font_name=font_name,
                  font_size=font_size, font_color=font_color,
                  text_alignment=text_alignment)
        if verbose:
            print(f'--> Watermarked: {i + 1} / {total}', end='\r')
    if verbose:
        print(f'--> Success! Find watermarked files in a directpry called:'
              f' {output_directory}')


def _watermark_oto(text='PDFPlay', target_file=None, output_file=None,
                   font_name='Helvetica-Bold', font_size='medium',
                   font_color='lightred', text_alignment='diagonal', verbose=False):
    watermark(text, target_file, output_file, font_name=font_name,
              font_size=font_size, font_color=font_color,
              text_alignment=text_alignment)
    if verbose:
        print(f'--> Success! Find watermarked file: {output_file}')


def _watermark(args=None):
    if args is None:
        args = parse_watermark_args()
    type_ = args.type
    del args.type
    del args.command
    type_map = dict(oto=_watermark_oto, otm=_watermark_otm, mto=_watermark_mto)
    type_map[type_](**vars(args))


def main():
    args = parse_user_args()
    debug = args.debug
    del args.debug
    command_map = dict(watermark=_watermark)
    try:
        command_map[args.command](args)
    except Exception as e:
        print(f'Error: {e}')
        if debug:
            raise e
