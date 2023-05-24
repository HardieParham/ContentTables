# Standard imports 
import os
import datetime

# External Imports

# Local Imports
from .models.content import Content
from .models.file import ContentFile
from .models.folder import ContentFolder, ContentSubFolder
from .extensions.formatting import format_folder
from .extensions.excel import Workbook




class App():
    def __init__(self) -> None:
        self.source_lang = str(input('Please input the 2-letter language code for this project: '))
        self.dest_lang = 'en'
        self.project_name = str(input('Please input the folder name to be used: '))
        self.template_name = 'template.xlsx'
        self.start_time = datetime.datetime.now()
        self.template = Workbook(self.template_name, self.project_name)


    def run(self) -> None:
        self.template.save_wb()
        self.loop()
        self.template.save_wb()
        print(f'This took {datetime.datetime.now()-self.start_time} seconds')


    def loop(self) -> None:
        """
        Main loop for the app. 

        Loops through all folders and files in the input folder.
        Converts these into python objects to be modified and translated.
        Edits the Excel template to include these objects.
        """
        for root, _, files in os.walk(self.project_name, topdown=True, followlinks=False):
            current_dir, level = format_folder(root)
            rel_dir = os.path.relpath(root, self.project_name)

            if level <= 2:
                row = ContentFolder(name=current_dir, level=level, path=rel_dir, src=self.source_lang, dest=self.dest_lang)
                self.template.apply_folder(row)

            if level > 2:
                row = ContentSubFolder(name=current_dir, level=level, path=rel_dir, src=self.source_lang, dest=self.dest_lang)
                self.template.apply_folder(row)

            for file in files:
                rel_file = os.path.join(rel_dir, file)
                row = ContentFile(name=file, dir=current_dir, path=rel_file, src=self.source_lang, dest=self.dest_lang)
                self.template.apply_file(row)
                
        self.template.apply_blank(bottom=True) #Add a blank row at end of file