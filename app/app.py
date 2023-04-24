# Standard imports 
import os

# External Imports

# Local Imports
from modules.excel import *
from modules.translate import *



def run():
    for root, dirs, files in os.walk('input', topdown=True, followlinks=False):
        path_list = root.split('\\')
        current_dir = path_list[-1]

        print(len(path_list))
        print(f'Root: {current_dir}')

        for file in files:
            print(file)