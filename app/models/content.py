from ..extensions.translate import translate

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