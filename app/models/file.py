from .content import Content


class ContentFile(Content):
    def __init__(self, name):
        super().__init__(name)
        self.pages = 0
        self.filetype = name.split('.')[-1]