#!/usr/bin/python3
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def combine_pdf(oddfile, evenfile, outfile):
    process_even(evenfile)

    # Combine files
    pdf_writer = PdfFileWriter()
    pdf_reader_odd = PdfFileReader(oddfile)
    pdf_reader_even = PdfFileReader(evenfile)

    for i in range(0, pdf_reader_odd.numPages):
        pdf_writer.addPage(pdf_reader_odd.getPage(i))
        
        if i < pdf_reader_even.numPages:
            pdf_writer.addPage(pdf_reader_even.getPage(i))

    with open(outfile, 'wb') as f:
        pdf_writer.write(f)

def process_even(pdfpath):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdfpath)

    for page in range(pdf_reader.numPages - 1, -1, -1):
        # Reverse order and rotate page
        pdf_writer.addPage(pdf_reader.getPage(page).rotateClockwise(180))

    with open(pdfpath, 'wb') as f:
        pdf_writer.write(f)

if __name__ == "__main__":
    oddfile = sys.argv[1]
    evenfile = sys.argv[2]
    outfile = sys.argv[3]
    combine_pdf(oddfile, evenfile, outfile)
