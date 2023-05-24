from openpyxl.styles import PatternFill, Border, Side

from .content import COLORS


class ContentBlank():
    def __init__(self, bottom) -> None:
        self.bottom = bottom
        self.border = self.set_borders()
        self.fill = PatternFill(patternType='solid', bgColor=COLORS['white'], fgColor=COLORS['white'])



    def set_borders(self) -> object:
        border_style = Side(style='thin', color=COLORS['black'])
        if self.bottom == False:    
            border = Border(left=border_style, right=border_style)
        elif self.bottom == True:
            border = Border(left=border_style, right=border_style, bottom=border_style)

        return border
