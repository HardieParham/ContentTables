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
        self.template_name = 'blank.xlsx' #'blank.xlsx'
        self.start_time = datetime.datetime.now()
        self.template = Workbook(self.template_name, self.project_name)



    def main_loop(self) -> None:
        self.template.save_wb()
        self.loop()
        self.template.save_wb()
        print(f'This took {datetime.datetime.now()-self.start_time} seconds')


    def loop(self):
        for root, _, files in os.walk(self.project_name, topdown=True, followlinks=False):
            current_dir, level = format_folder(root)
            row = ContentFolder(name=current_dir, level=level)
            self.template.apply_folder(row)


            for file in files:
                rel_dir = os.path.relpath(root, self.project_name)
                rel_file = os.path.join(rel_dir, file)
                print(rel_file)
                row = ContentFile(name=file, dir=current_dir, path=rel_file)
                print(file)
                self.template.apply_file(row)

