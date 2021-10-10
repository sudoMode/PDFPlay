from pdf_play.core._pdf import PDF

# __all__ = ['PDF']
client = PDF(debug=True)


def watermark(text, target_file, output_file, **style):
    print(f'Text: {text}')
    print(f'Target: {target_file}')
    print(f'Output: {output_file}')
    print(f'Style: {style}')
    print('---------------------------------')
    client.apply_watermark(text, target_file, output_file, **style)
    return True


__all__ = ['watermark']
