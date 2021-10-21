from os import getcwd, makedirs
from os.path import join, sep, isdir
from pathlib import Path

import pandas as pd


def is_pdf(path):
    return path.endswith('.pdf')


def flatten(nested_list):
    values = []
    for i in nested_list:
        if isinstance(i, list):
            for j in i:
                values.append(j)
        else:
            values.append(i)
    return values


def read_file(file, header=1):
    # print(f'reading: {file}')
    reader = pd.read_csv if file.endswith('.csv') else pd.read_excel
    return reader(file, header=header)


def generate_watermark_input(args):
    # print('gen...')
    file_names, watermark_texts = [], []
    if args.text_data is not None:
        # TODO: check dropna
        data = read_file(args.text_data)
        # data.dropna(inplace=True)
        # print(data)
        data.columns = map(lambda x: x.lower().replace(' ', '_'), data.columns)
        # print(data)
        if args.text_header:
            header = args.text_header.lower().replace(' ', '_')
            watermark_texts = data[header].tolist()
        else:
            # print(22)
            # print(data)
            watermark_texts = data.iloc[:, 0].tolist()
            # print(watermark_texts)
        if args.name_header:
            header = args.name_header.lower().replace(' ', '_')
            file_names = data[header].tolist()
        else:
            file_names = list(map(lambda x: x.splitlines()[0], watermark_texts))

    if args.texts:
        watermark_texts.extend(args.texts)
        file_names.extend(list(map(lambda x: x, args.texts)))
    data = dict(zip(file_names, watermark_texts))
    # print('*************************')
    # print(data)
    return data


def validate_otm(args):
    if args.output_directory is None:
        args.output_directory = join(getcwd(), 'watermarked')
        if not isdir(args.output_directory):
            makedirs(args.output_directory)
    print(f'Watermarked files will be saved to: {args.output_directory}')


def validate_mto(args):
    validate_otm(args)
    # print(f'came...: {args}')
    args.watermark_input = generate_watermark_input(args)


def validate_oto(args):
    if args.output_file is None:
        base = Path(args.target_file).parent.resolve()
        file_name = args.target_file.split(sep)[-1]
        name, extension = file_name.split('.')
        args.output_file = join(base, f'{name}_watermarked.{extension}')
    print(f'Watermarked files will be saved to: {args.output_file}')


def update_args(args):
    # update rgb values
    if args.rgb != (0, 0, 0):
        if len(args.rgb) > 3:
            raise ValueError(f'RGB expects 3 values, received: {len(args.rgb)} -> '
                             f'{args.rgb}')
        while len(args.rgb) < 3:
            args.rgb.append(0)
    if args.type == 'oto':
        validate_oto(args)
    if args.type == 'otm':
        validate_otm(args)
    if args.type == 'mto':
        validate_mto(args)
    return args


def validate_args(parser, args):
    if args.command is None:
        parser.print_help()
        exit(0)
    else:
        if args.type is None:
            print('\n--> User must specify the mode of operation. '
                  f'Get help: {args.command} -h')
            exit(0)
