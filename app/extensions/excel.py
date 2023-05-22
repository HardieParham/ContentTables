# Standard imports
import re
import os
import logging
from copy import copy


# External Imports
import openpyxl
from openpyxl.styles import PatternFill, Color, Border, cell_style, Alignment, Side
from openpyxl.utils import get_column_letter


# Local Imports
from ..models.blank import ContentBlank


class Workbook():
    def __init__(self, template_name, project_name):
        self.name = template_name
        self.project_name = project_name
        self.new_name = f'ContentTable.xlsx'
        self.wb = openpyxl.load_workbook(f"templates/{self.name}")
        self.ws = self.wb.worksheets[0]
        self.row_counter = 26 # to start on the correct row


    def save_wb(self):
        self.wb.save(f'{self.project_name}/{self.new_name}')
        print('saved')


    # def excel_loop(self):
    #     self.save_wb()
    #     for i, item in enumerate(self.item_list):
    #         print(f'{i}: {item}')
    #         adj_row = i + 28
    #         text = self.ws['B' + str(28)]
    #         # i - row number
    #         # col A - file type
    #         # col B - name and link
    #         # col H - new_name and link
    #         # col N - number of pages (1 for now)
    #         self.ws['A' + str(adj_row)].value = item.filetype
    #         self.ws['B' + str(adj_row)].value = item.oldname
    #         self.ws['C' + str(adj_row)].value = item.newname
    #         self.ws['D' + str(adj_row)].value = '1'
    #     text = self.ws['B' + str(28)]
    #     self.save_wb()


    def apply_blank(self):
        item = ContentBlank()
        self.ws['A' + str(self.row_counter)].border = item.border
        self.ws['A' + str(self.row_counter)].fill = item.fill

        self.ws['B' + str(self.row_counter)].border = item.border
        self.ws['B' + str(self.row_counter)].fill = item.fill

        self.ws['C' + str(self.row_counter)].border = item.border
        self.ws['C' + str(self.row_counter)].fill = item.fill

        self.ws['D' + str(self.row_counter)].border = item.border
        self.ws['D' + str(self.row_counter)].fill = item.fill
        self.row_counter += 1



    def apply_folder(self, item):
        self.apply_blank()
        print(f'{self.row_counter}: {item.oldname}')

        self.ws['A' + str(self.row_counter)].value = item.filetype
        self.ws['A' + str(self.row_counter)].alignment = item.alignment
        self.ws['A' + str(self.row_counter)].border = item.border
        self.ws['A' + str(self.row_counter)].fill = item.fill
        self.ws['A' + str(self.row_counter)].font = item.font

        self.ws['B' + str(self.row_counter)].value = item.oldname
        self.ws['B' + str(self.row_counter)].hyperlink = item.path
        self.ws['B' + str(self.row_counter)].alignment = item.alignment
        self.ws['B' + str(self.row_counter)].border = item.border
        self.ws['B' + str(self.row_counter)].fill = item.fill
        self.ws['B' + str(self.row_counter)].font = item.font

        self.ws['C' + str(self.row_counter)].value = item.newname
        self.ws['C' + str(self.row_counter)].alignment = item.alignment
        self.ws['C' + str(self.row_counter)].border = item.border
        self.ws['C' + str(self.row_counter)].fill = item.fill
        self.ws['C' + str(self.row_counter)].font = item.font

        self.ws['D' + str(self.row_counter)].value = 1
        self.ws['D' + str(self.row_counter)].alignment = item.alignment
        self.ws['D' + str(self.row_counter)].border = item.border
        self.ws['D' + str(self.row_counter)].fill = item.fill
        self.ws['D' + str(self.row_counter)].font = item.font
        self.row_counter += 1


    def apply_file(self, item):
        print(f'{self.row_counter}: {item.oldname}')
        self.ws['A' + str(self.row_counter)].value = item.filetype
        self.ws['A' + str(self.row_counter)].alignment = item.alignment
        self.ws['A' + str(self.row_counter)].border = item.border
        self.ws['A' + str(self.row_counter)].fill = item.fill
        self.ws['A' + str(self.row_counter)].font = item.font

        self.ws['B' + str(self.row_counter)].value = item.oldname
        self.ws['B' + str(self.row_counter)].hyperlink = item.path
        # print(f'path: {item.path}')
        # print(f'hyperlink: {self.ws["B" + str(self.row_counter)].hyperlink.target}')
        self.ws['B' + str(self.row_counter)].alignment = item.alignment
        self.ws['B' + str(self.row_counter)].border = item.border
        self.ws['B' + str(self.row_counter)].fill = item.fill
        self.ws['B' + str(self.row_counter)].font = item.font

        self.ws['C' + str(self.row_counter)].value = item.newname
        self.ws['C' + str(self.row_counter)].alignment = item.alignment
        self.ws['C' + str(self.row_counter)].border = item.border
        self.ws['C' + str(self.row_counter)].fill = item.fill
        self.ws['C' + str(self.row_counter)].font = item.font

        self.ws['D' + str(self.row_counter)].value = 1
        self.ws['D' + str(self.row_counter)].alignment = item.alignment
        self.ws['D' + str(self.row_counter)].border = item.border
        self.ws['D' + str(self.row_counter)].fill = item.fill
        self.ws['D' + str(self.row_counter)].font = item.font

        # cell = self.ws['A' + str(self.row_counter)]
        # print(cell)
        self.row_counter += 1
