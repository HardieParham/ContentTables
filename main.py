# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Hello World'

# if __name__  == '__main__':
#     app.run(debug=True)


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