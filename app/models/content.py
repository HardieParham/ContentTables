class Content():
    content_list = []
    def __init__(self, name):
        self.oldname = name
        self.newname = ''
        self.excelrow = 0
        Content.content_list.append(self.oldname)

    def __repr__(self):
        return f'{self.oldname}'