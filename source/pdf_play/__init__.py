from os.path import join
from os.path import sep

from pdf_play import __settings__ as settings
from pdf_play.core import watermark
from pdf_play.helpers import parse_user_args
from pdf_play.helpers import parse_watermark_args


def _watermark_mto(**kwargs):
    print(f'called: {kwargs}')

    texts = kwargs['texts']
    target_file = kwargs['target_file']
    output_directory = kwargs['output_directory']
    del kwargs['texts']
    del kwargs['target_file']
    total = len(texts)
    if kwargs['verbose']:
        print(f'--> Received {total} watermark texts...')
    for i, item in enumerate(texts):
        output_file = join(output_directory, f'{item[0]}.pdf')
        text = item[1]
        watermark(text, target_file, output_file, **kwargs)
        if kwargs['verbose']:
            print(f'--> Watermarked: {i + 1} / {total}', end='\r')
    if kwargs['verbose']:
        print(f'--> Success! Find watermarked files in a directpry called:'
              f' {output_directory}')


def _watermark_otm(**kwargs):
    text = kwargs['text']
    target_files = kwargs['target_files']
    output_directory = kwargs['output_directory']
    total = len(target_files)
    if kwargs['verbose']:
        print(f'--> Received {total} target files...')
    for i, target_file in enumerate(target_files):
        name_and_extension = target_file.split(sep)[-1]
        name, extension = name_and_extension.split('.')
        output_file = join(output_directory, f'{name}_watermarked.{extension}')
        watermark(text, target_file, output_file, **kwargs)
        if kwargs['verbose']:
            print(f'--> Watermarked: {i + 1} / {total}', end='\r')
    if kwargs['verbose']:
        print(f'--> Success! Find watermarked files in a directpry called:'
              f' {output_directory}')


def _watermark_oto(**kwargs):
    text = kwargs['text']
    target_file = kwargs['target_file']
    output_file = kwargs['output_file']
    watermark(text, target_file, output_file, **kwargs)
    if kwargs['verbose']:
        print(f'--> Success! Find watermarked file: {output_file}')


def _watermark(**kwargs):
    if kwargs is None:
        # TODO: move it to parser
        kwargs = vars(parse_watermark_args())
    type_ = kwargs.get('type', 'oto')
    del kwargs['type']
    del kwargs['command']
    type_map = dict(oto=_watermark_oto, otm=_watermark_otm, mto=_watermark_mto)
    type_map[type_](**kwargs)


def main():
    args = parse_user_args()
    print('---------------------------')
    print(f'User Args: {args}')
    # return
    debug = args.debug
    command_map = dict(watermark=_watermark)
    try:
        command_map[args.command](**vars(args))
    except Exception as e:
        print(f'Error: {e}')
        if debug:
            raise e


if __name__ == '__main__':
    main()
