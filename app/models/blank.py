from openpyxl.styles import PatternFill, Color, Border, cell_style, Alignment, Side, Font

from .content import COLORS


class ContentBlank():
    def __init__(self):
        self.border = self.set_borders()
        self.fill = PatternFill(patternType='solid', bgColor=COLORS['white'], fgColor=COLORS['white'])



    def set_borders(self):
        vertical_style = Side(style='thin', color=COLORS['black'])
        border = Border(left=vertical_style, right=vertical_style)
        return border
