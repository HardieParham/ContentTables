print('Hello World')


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




file = ['id', 'folder', 'filename', ]
folder = ['id', 'name', 'above_folder', 'sub_folders', 'file_list']




class folder():
    folder_list = []
    def __init__(self, name: str, folder_link: int, id: int):
        self.name = name
        self.folder_link = folder_link
        self.id = id
        self.sub_folders = []
        folder.folder_list.append(self)


    def __repr__(self):
        return f'{self.id} - {self.name} - Link: {self.folder_link}'


    def add_sub_folder(self, thing):
        self.sub_folders.append(thing)


class file():
    def __init__(self, name: str, folder: str):
        self.name = name
        self.folder = folder



# for root, dirs, files in os.walk(current_dir, topdown=True, followlinks=False):
#     for dir in dirs:
#         current_dir = root.split('\\')[-1]
#         folder(dir, current_dir, id)
#         id += 1

#     for file in files:
#         print(f'file: {file}, Root: {root}, Dir: {current_dir}')

# print(folder.folder_list)




# current_dir = 'input'
"""
id = 0
folder_todo_list = ['input']



for root, dirs, files in os.walk(folder_todo_list[0], topdown=True, followlinks=False):
    if root != folder_todo_list[0]:
        current_dir = root.split('\\')[-1]
        print(current_dir)
        del folder_todo_list[0]
    print(root)
    time.sleep(1)

    for file in files:
        print(file)
        time.sleep(1)

    for dir in dirs:
        print(dir)
        folder_todo_list.append(dir)
        time.sleep(1)

print(folder_todo_list)

"""


test = {
    'input':
    {
        'files': ['item1', 'item2'],
        'dir': {
            'sub-folder1': {
                'files': ['item1'],
                'dir': {
                    'sub-sub-folder': {
                        'files': ['item1'],
                        'dir': {}
                    }
                }
            },

            'sub-folder2': {
                'files': ['item1'],
                'dir': {}
            }

        }
    }
}





# // NEW
class Folder():
    def __init__(self, name, ):
        self.id = ''
        self.name = ''
        self.level = ''
        self.file_list = []
        pass





for root, dirs, files in os.walk('input', topdown=True, followlinks=False):
    
    # Finding Folder level
    path_list = root.split('\\')
    current_dir = path_list[-1]
    print(len(path_list))

    print(f'Root: {current_dir}')


    for file in files:
        print(file)