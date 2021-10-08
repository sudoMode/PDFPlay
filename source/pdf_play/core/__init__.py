from pdf_play.core._pdf import PDF

# __all__ = ['PDF']
client = PDF()


def watermark(text, target_file, output_file, **style):
    client.apply_watermark(text, target_file, output_file, **style)


__all__ = ['watermark']
