# pip install -r /path/to/requirements.txt


# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Hello World'

# if __name__  == '__main__':
#     app.run(debug=True)


"""
PLAN

Take template excel file

for items in a folder, add to file
    also, translate item too

update generic items in file (photos, misc info)




Detailed plan:


open template file

save as new

set input folder as current working directory

os walk thru the folder

"""





import time
import re
import openpyxl
import os
import json
import googletrans


# file = ['id', 'folder', 'filename']
# folder = ['id', 'name', '']

# test = {
#         'name': 'input',
#         'files': ['item1', 'item2'],
#         'dir': ['subfolder1', 'subfolder2']
#         }


# import app.app as app

# if __name__ == '__main__':
#     app.run()






"""
Process:

1)
Open template.xlsx
create copy of template
save new copy and set to working file

2)
create list of file/folder names
Loop thru working directory
State folder level and name. append to list
for files in folder, append to list.

OR

don't save in lists at all, immediately add to excel file
use the file as the storage medium

2.1)
if filetype = docx
open file, save number of total pages

2.2)
if filetype = pdf
open file, save number of pages

2.3)
if filetype = xlsx
open file, save number of worksheets

2.4)
if filetype = cad
pages = 1

2.5) 
else
pages = 1 (or unknown?)

3)
create translated dict
loop thru file/folder list
key, value pair of original and translated

4)
Open template.xlsx
create copy of template
save new copy and set to working file





"""

class Template():
    def __init__(self):
        self.name = ''
        self.input = 'input'

    def loop(self):
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




   


class Content():
    content_list = []
    def __init__(self, name):
        self.oldname = name
        self.newname = ''
        self.excelrow = 0
        Content.content_list.append(self.oldname)
    

class ContentFolder(Content):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level


class ContentFile(Content):
    def __init__(self, name):
        super().__init__(name)
        self.pages = 0
        self.filetype = name.split('.')[-1]



if __name__ == "__main__":
    looper = Template()
    looper.loop()
    print (Content.content_list)