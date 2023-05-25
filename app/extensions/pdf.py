from PyPDF2 import PdfReader


def get_pages_num(item: object) -> int:
    try:
        reader = PdfReader(f".\\{item.root}\\{item.path}")
        number_of_pages = len(reader.pages)
        return number_of_pages
    except:
        return 1
