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


file = ['id', 'folder', 'filename']
folder = ['id', 'name', '']

test = {
        'name': 'input',
        'files': ['item1', 'item2'],
        'dir': ['subfolder1', 'subfolder2']
        }


import app.app as app

if __name__ == '__main__':
    app.run()