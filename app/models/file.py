import os

from .content import Content


class ContentFile(Content):
    def __init__(self, name):
        self.filename, self.filetype = os.path.splitext(name)
        print(self.filename)
        super().__init__(self.filename)
        self.pages = 0
