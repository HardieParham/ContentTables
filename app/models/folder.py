from .content import Content


class ContentFolder(Content):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level