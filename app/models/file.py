# Standard Imports
import os

# Local Imports
from .content import Content


class ContentFile(Content):
    def __init__(self, name):
        self.filename, self.filetype = os.path.splitext(name)
        super().__init__(self.filename)
        self.pages = 0
