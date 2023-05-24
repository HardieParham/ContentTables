from openpyxl.styles import Color

from ..extensions.translate import translate

COLORS = {
    'white': Color(rgb='00FFFFFF'),
    'red': Color(rgb='00FF0000'),
    'black': Color(rgb='00000000'),
    'blue': Color(rgb='000000FF'),
    'brown': Color(rgb='00800000'),
}

class Content():
    content_list = []
    def __init__(self, name: str, src: str, dest: str) -> None:
        self.oldname = name
        self.newname = translate(name, src=src, dest=dest)
        self.excelrow = 0
        Content.content_list.append(self.oldname)
        print(f'{self.oldname}: {self.newname}')

    def __repr__(self):
        return f'{self.oldname}'