import os

from openpyxl.styles import PatternFill, Color, Border, cell_style, Alignment, Side, Font

from .content import Content, COLORS


class ContentFolder(Content):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level
        self.filetype = 'Folder'
        self.border = self.set_borders()
        self.font = self.set_font()
        self.fill = PatternFill(patternType='solid', bgColor=COLORS['red'], fgColor=COLORS['red'])
        self.alignment = Alignment(horizontal='center', vertical='center')


    def set_borders(self):
        vertical_style = Side(style='thick', color=COLORS['black'])
        border = Border(left=vertical_style, right=vertical_style, top=vertical_style)
        return border


    def set_font(self):
        name='Arial'
        size = 10
        font_style = Font(name=name, color=COLORS['white'], size=size)
        return font_style