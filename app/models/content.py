import os

from openpyxl.styles import PatternFill, Color, Border, cell_style, Alignment, Side, Font

from ..extensions.translate import translate

COLORS = {
    'white': Color(rgb='00FFFFFF'),
    'red': Color(rgb='00FF0000'),
    'black': Color(rgb='00000000'),
}

class Content():
    content_list = []
    def __init__(self, name):
        self.oldname = name
        self.newname = translate(name)
        self.excelrow = 0
        Content.content_list.append(self.oldname)
        print(f'{self.oldname}: {self.newname}')

    def __repr__(self):
        return f'{self.oldname}'