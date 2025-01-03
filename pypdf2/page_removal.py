from PyPDF2 import PdfReader, PdfWriter


def remove_selective_pdf_pages(input_path, output_path, page_list):
    """
    Removing selective pdf pages using pypdf2
    args:
        input_path: [str]: Path to input file
        output_path: [str]: Path to output file
        page_list: [list]: List of pages to remove
    return:
        None
    """
    # open the original PDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # iterate through the original PDF pages
    for page_num in range(len(reader.pages)):
        # Add pages that are not in the pages_to_remove list
        if page_num not in pages_to_remove:
            writer.add_page(reader.pages[page_num])

    # write the new PDF to a file
    with open(output_pdf_path, 'wb') as output_pdf_file:
        writer.write(output_pdf_file)


if __name__ == "__main__":
    # path to the input PDF
    input_pdf_path = "Downloads/abc.pdf"
    # path to the output PDF
    output_pdf_path = "Downloads/abc_edited.pdf"
    pages_to_remove = [2, 9, 21, 75]
    pages_to_remove = [x - 1 for x in pages_to_remove]
    # -1 bcz it works on 0-index
    remove_selective_pdf_pages(input_pdf_path, output_pdf_path, pages_to_remove)
    print(f"Pages {pages_to_remove} removed from {input_pdf_path} and saved to {output_pdf_path}")

