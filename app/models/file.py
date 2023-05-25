import os

from openpyxl.styles import PatternFill, Color, Border, cell_style, Alignment, Side, Font

from .content import Content, COLORS
from ..extensions import pdf


class ContentFile(Content):
    def __init__(self, name: str, dir: str, path: str, src: str, dest: str, root:str) -> None:
        self.filename, self.filetype = os.path.splitext(name)
        super().__init__(self.filename, src, dest)
        self.root = root
        self.dir = dir
        self.path = str(path)
        self.pages = self.set_pages()
        self.border = self.set_borders()
        self.font = self.set_font()
        self.fill = PatternFill(patternType='solid', bgColor=COLORS['white'], fgColor=COLORS['white'])
        self.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)


    def set_borders(self) -> object:
        vertical_style = Side(style='thin', color=COLORS['black'])
        border = Border(left=vertical_style, right=vertical_style)
        return border


    def set_font(self) -> object:
        name='Arial'
        size = 11
        font_style = Font(name=name, color=COLORS['black'], size=size)
        return font_style
    

    def set_pages(self) -> int:
        if self.filetype == '.pdf':
            return pdf.get_pages_num(self)
        else:
            return 1

