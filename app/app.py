# Standard imports 
import os

# External Imports

# Local Imports
from .models.content import Content
from .models.file import ContentFile
from .models.folder import ContentFolder
from .extensions.formatting import format_folder
from .extensions.excel import *
from .extensions.translate import translate
from .data import char_to_replace, data




class App():
    def __init__(self) -> None:
        self.name = 'blank.xlsx'
        self.input = 'input'
        # self.translator = Translator()
        self.content_list = []



    def main_loop(self) -> None:
        """
        TODO:
        
        Best practice would be to make "main_loop" all one loop, rather than 3 individual loops.
        If free time is available, fix this.
        """
        self.read_loop()
        self.translate_loop()
        self.excel_loop()


    def read_loop(self) -> None:
        for root, _, files in os.walk(self.input, topdown=True, followlinks=False):
            current_dir, level = format_folder(root)
            self.content_list.append(ContentFolder(name=current_dir, level=level))

            for file in files:
                self.content_list.append(ContentFile(name=file))


    def translate_loop(self) -> None:
        for item in self.content_list:
            item.newname = translate(text=item.oldname)


    def excel_loop(self):
        pass


# Read Loop
# Translate Loop
# Print to XL Loop
