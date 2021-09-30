# -*- coding: utf-8 -*-
from __settings__ import *
from io import BytesIO
from reportlab.pdfgen.canvas import Canvas
# noinspection PyProtectedMember
from PyPDF4 import PdfFileReader
# noinspection PyProtectedMember
from PyPDF4 import PdfFileWriter
from reportlab.lib.pagesizes import A4


def create_watermark(wm_text):
    """
        Creates a watermark template.
    """
    # Generate the output to a memory buffer
    output_buffer = BytesIO()
    c = Canvas(output_buffer, pagesize=A4)
    c.setFont(FONT_NAME, FONT_SIZE)
    c.setFillColor(COLOR)
    # Rotate according to the configured parameter
    c.rotate(ROTATION_ANGLE)
    # Position according to the configured parameter
    c.drawString(POSITION_X, POSITION_Y, wm_text)
    c.save()
    return output_buffer


def watermark_pdf(input_file, wm_text):
    """
        Adds watermark to a pdf file.
    """
    wm_buffer = create_watermark(wm_text)
    wm_reader = PdfFileReader(wm_buffer)
    pdf_reader = PdfFileReader(input_file, strict=False)
    pdf_writer = PdfFileWriter()
    output_buffer = BytesIO()
    print(pdf_reader.getNumPages())
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        page.mergePage(wm_reader.getPage(0))
        pdf_writer.addPage(page)

    pdf_writer.write(output_buffer)
    pdf_reader.stream.close()

    with open(f'{wm_text}.pdf', 'wb') as f:
        f.write(output_buffer.getbuffer())


def main():
    pdf = INPUT_FILE
    wm_text = 'best wmatermark ever!!!!'
    watermark_pdf(pdf, wm_text)


if __name__ == '__main__':
    main()
