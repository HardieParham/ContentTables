import os

from openpyxl.styles import PatternFill, Color, Border, cell_style, Alignment, Side, Font

from .content import Content, COLORS


class ContentFolder(Content):
    def __init__(self, name, level, path):
        super().__init__(name)
        self.level = level
        self.filetype = 'Folder'
        self.path = str(path)
        self.border = self.set_borders()
        self.font = self.set_font()
        self.fill = PatternFill(patternType='solid', bgColor=COLORS['red'], fgColor=COLORS['red'])
        self.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)


    def set_borders(self):
        vertical_style = Side(style='thin', color=COLORS['black'])
        border = Border(left=vertical_style, right=vertical_style, top=vertical_style)
        return border


    def set_font(self):
        name='Arial'
        size = 12
        font_style = Font(name=name, color=COLORS['white'], size=size)
        return font_style
    



class ContentSubFolder(Content):
    def __init__(self, name, level, path):
        super().__init__(name)
        self.level = level
        self.filetype = int(level-1)*'S' + ' Folder'
        self.path = str(path)
        self.border = self.set_borders()
        self.font = self.set_font()
        self.fill = PatternFill(patternType='solid', bgColor=COLORS['white'], fgColor=COLORS['white'])
        self.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)


    def set_borders(self):
        vertical_style = Side(style='thin', color=COLORS['black'])
        border = Border(left=vertical_style, right=vertical_style, top=vertical_style)
        return border


    def set_font(self):
        name='Arial'
        size = 12
        font_style = Font(name=name, color=COLORS['red'], size=size)
        return font_style