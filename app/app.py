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

    def loop(self) -> None:
        for root, dirs, files in os.walk(self.input, topdown=True, followlinks=False):
            path_list = root.split('\\')
            current_dir = path_list[-1]

            level = len(path_list)
            print(f'Root: {current_dir}, lvl: {level}')

            folder = ContentFolder(name=current_dir, level=level)
            #Content.content_list.append(f'{len(path_list)} - {current_dir}')

            for file in files:
                print(file)
                new = ContentFile(name=file)
                print(new.filetype)