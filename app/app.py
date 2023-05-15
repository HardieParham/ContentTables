# Standard imports 
import os

# External Imports

# Local Imports
from .models.content import Content
from .models.file import ContentFile
from .models.folder import ContentFolder
from .extensions.excel import *
from .extensions.translate import Translator
from .data import char_to_replace, data




class App():
    def __init__(self) -> None:
        self.name = 'blank.xlsx'
        self.input = 'input'
        self.translator = Translator(src=data['src'], dest=data['dest'])
        self.content_list = []

    def read_loop(self) -> None:
        for root, _, files in os.walk(self.input, topdown=True, followlinks=False):
            current_dir, level = self.format_folder(root)
            self.content_list.append(ContentFolder(name=current_dir, level=level))

            for file in files:
                self.content_list.append(ContentFile(name=file))

        print(self.content_list)



    def main_loop(self) -> None:
        for root, dirs, files in os.walk(self.input, topdown=True, followlinks=False):
            print('hi')

        # for thing in things:
        #     read(thing)
        #     translate(thing)
        #     xlprint(thing)


    def format_folder(self, root: str) -> tuple:
        """
        Function for formating folder paths, returning the name and level of the lowest folder 
        
        :param root: path string returned from the os.walk function
        :type root: string

        :rtype: tuple
        """
        folder_path = root.split('\\')
        current_dir = folder_path[-1]
        level = len(folder_path)
        return (current_dir, level)



    def read_content():
        pass



# Read Loop
# Translate Loop
# Print to XL Loop
