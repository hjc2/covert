from pypdf import PdfReader, PdfWriter
import zlib
import base64

def embed_data_in_pdf(input_pdf, output_pdf, hidden_data):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)

    compressed_data = zlib.compress(hidden_data.encode('utf-8'))
    encoded_data = base64.b64encode(compressed_data).decode('utf-8')

    metadata = reader.metadata
    writer.add_metadata({
        '/Title': metadata.title + ' ' + encoded_data
    })

    with open(output_pdf, 'wb') as out_file:
        writer.write(out_file)

def extract_data_from_pdf(input_pdf):
    reader = PdfReader(input_pdf)
    metadata = reader.metadata
    title = metadata.title

    encoded_data = title.split(' ')[-1]
    compressed_data = base64.b64decode(encoded_data)
    hidden_data = zlib.decompress(compressed_data).decode('utf-8')

    return hidden_data

if __name__ == "__main__":

    hidden_data = "This is a secret"

    embed_data_in_pdf("thepdf.pdf", "datapdf.pdf", hidden_data)

    ext = extract_data_from_pdf("datapdf.pdf")

    print(ext)