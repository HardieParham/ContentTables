# Standard imports 
import os
import datetime

# External Imports

# Local Imports
from .models.content import Content
from .models.file import ContentFile
from .models.folder import ContentFolder
from .extensions.formatting import format_folder
from .extensions.excel import Workbook




class App():
    def __init__(self) -> None:
        self.project_name = 'input' # Name the input folder this as well
        self.template_name = 'blank.xlsx'
        self.content_list = []



    def main_loop(self) -> None:
        """
        TODO:
        
        Best practice would be to make "main_loop" all one loop, rather than 2 individual loops.
        If free time is available, fix this.
        """
        start = datetime.datetime.now()
        print('reading and Translating')
        # self.read_loop()
        print('To excel')
        self.excel_loop()
        print(f'This took {datetime.datetime.now()-start} seconds')


    def read_loop(self) -> None:
        for root, _, files in os.walk(self.project_name, topdown=True, followlinks=False):
            current_dir, level = format_folder(root)
            self.content_list.append(ContentFolder(name=current_dir, level=level))

            for file in files:
                self.content_list.append(ContentFile(name=file))
                print(file)



    def excel_loop(self) -> None:
        template = Workbook(self.template_name, self.project_name, self.content_list)
        template.excel_loop()
        print('done')
