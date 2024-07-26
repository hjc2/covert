from PyPDF2 import PdfReader, PdfWriter

def modify_pdf_header(input_pdf, output_pdf, new_header):
    # Load the PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Remove existing header if present
    metadata = reader.metadata
    if '/Header' in metadata:
        del metadata['/Header']

    # Add new header
    # metadata['/Header'] = new_header

    customHeader = {
        '/Ascent': 'Your Custom Header Value'
    }

    writer.add_metadata(customHeader)
    # # Copy all pages from the input PDF to the new PDF
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        writer.add_page(page)

    # Save the modified PDF
    with open(output_pdf, 'wb') as out_file:
        writer.write(out_file)

# Example usage
input_pdf_path = "IEEE_MASS.pdf"
output_pdf_path = "output.pdf"
new_header = "Your"

modify_pdf_header(input_pdf_path, output_pdf_path, new_header)
