from pdf_play.core._pdf import PDF

client = PDF(debug=True)


def watermark(wm_text, file_to_watermark, file_to_save_it_as, **style):
    print(f'LL: {locals()}')
    client.apply_watermark(wm_text, file_to_watermark, file_to_save_it_as, **style)
    return True


__all__ = ['watermark']
