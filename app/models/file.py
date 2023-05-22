# Standard Imports
import os

# External Imports
from openpyxl.styles import PatternFill, Color, Border, cell_style, Alignment, Side, Font

# Local Imports
from .content import Content, COLORS




class ContentFile(Content):
    def __init__(self, name, dir, path):
        self.filename, self.filetype = os.path.splitext(name)
        super().__init__(self.filename)
        self.dir = dir
        self.pages = 1
        self.path = str('\\' + path)
        self.border = self.set_borders()
        self.font = self.set_font()
        self.fill = PatternFill(patternType='solid', bgColor=COLORS['white'], fgColor=COLORS['white'])
        self.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)


    def set_borders(self):
        vertical_style = Side(style='thin', color=COLORS['black'])
        border = Border(left=vertical_style, right=vertical_style)
        return border


    def set_font(self):
        name='Arial'
        size = 12
        font_style = Font(name=name, color=COLORS['black'], size=size)
        return font_style

