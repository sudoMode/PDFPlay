from pdf_play.core._pdf import PDF

# __all__ = ['PDF']
client = PDF(debug=True)


def watermark(text, target_file, output_file, **style):
    client.apply_watermark(text, target_file, output_file, **style)
    return True


__all__ = ['watermark']
