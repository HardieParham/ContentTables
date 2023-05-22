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
        self.new_name = f'{project_name}.xlsx'
        self.wb = openpyxl.load_workbook(f"templates/{self.name}")
        self.ws = self.wb.worksheets[0]
        self.row_counter = 26 # to start on the correct row


    def save_wb(self):
        self.wb.save(f'input/{self.new_name}')
        print('saved')


    def excel_loop(self):
        self.save_wb()
        for i, item in enumerate(self.item_list):
            print(f'{i}: {item}')
            adj_row = i + 28
            text = self.ws['B' + str(28)]
            # i - row number
            # col A - file type
            # col B - name and link
            # col H - new_name and link
            # col N - number of pages (1 for now)
            self.ws['A' + str(adj_row)].value = item.filetype
            self.ws['B' + str(adj_row)].value = item.oldname
            self.ws['C' + str(adj_row)].value = item.newname
            self.ws['D' + str(adj_row)].value = '1'
        text = self.ws['B' + str(28)]
        self.save_wb()


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
        # self.ws['B' + str(self.row_counter)].hyperlink = item.path
        self.ws['B' + str(self.row_counter)].alignment = item.alignment
        self.ws['B' + str(self.row_counter)].border = item.border
        self.ws['B' + str(self.row_counter)].fill = item.fill
        self.ws['B' + str(self.row_counter)].font = item.font

        self.ws['C' + str(self.row_counter)].value = item.newname
        self.ws['C' + str(self.row_counter)].alignment = item.alignment
        self.ws['C' + str(self.row_counter)].border = item.border
        self.ws['C' + str(self.row_counter)].fill = item.fill
        self.ws['C' + str(self.row_counter)].font = item.font

        self.ws['D' + str(self.row_counter)].value = '1'
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
        self.ws['B' + str(self.row_counter)].alignment = item.alignment
        self.ws['B' + str(self.row_counter)].border = item.border
        self.ws['B' + str(self.row_counter)].fill = item.fill
        self.ws['B' + str(self.row_counter)].font = item.font

        self.ws['C' + str(self.row_counter)].value = item.newname
        self.ws['C' + str(self.row_counter)].alignment = item.alignment
        self.ws['C' + str(self.row_counter)].border = item.border
        self.ws['C' + str(self.row_counter)].fill = item.fill
        self.ws['C' + str(self.row_counter)].font = item.font

        self.ws['D' + str(self.row_counter)].value = '1'
        self.ws['D' + str(self.row_counter)].alignment = item.alignment
        self.ws['D' + str(self.row_counter)].border = item.border
        self.ws['D' + str(self.row_counter)].fill = item.fill
        self.ws['D' + str(self.row_counter)].font = item.font

        # cell = self.ws['A' + str(self.row_counter)]
        # print(cell)
        self.row_counter += 1














"""
Base Class to work with Excel Documents

Methods to Load and save documents
Methods to loop thru entire word documents to update Text Class
"""
class OLD_Workbook():
    def __init__(self, file):
        self.name = file
        self.new_name = 'ENG_' + file
        self.wb = self.load_wb()
        self.ws_titles = {}


    def load_wb(self):
        wb = openpyxl.load_workbook(f"input/{self.name}")
        self.log_change(content=f'Starting translations for {self.name}')
        return wb


    def save_wb(self):
        self.wb.save(f'output/{self.new_name}')


    def log_change(self, content):
        with open('data/log.txt', 'a') as f:
            f.write(f'\n {content}')


    """
    Method to find the last cell (Row and column) that a value occurs
    NOTE: This is just the last column and last row that conatin a value. A value may not necessarily be at the row-column combination specified.
    e.g. Last item by column is in Z1, last item by row is in B 15, This function would return Z-15, even though there is not a value in that cell.
    """
    def get_lastcell(self):
            cols = (tuple(self.ws.columns))
            row=""
            col=""

            try:
                last_cell = str(cols[-1][-1])

                # Seperates the last cell's Letter Column and Number Row
                # NOTE Cell starts with a '.', so avoid '.' in the WS title 
                try:
                    split = last_cell.split("'.")
                except:
                    print("WorkSheet Name Error! Change worksheet name to avoid the following character combination '.")
                
                position = split[1]
                for item in position:
                    if item in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"):
                        col += item
                    elif item == ">":
                        pass
                    else:
                        row += item

                #Converting Column string into integer
                input = col.lower()
                output = []
                for character in input:
                    number = ord(character) - 96
                    output.append(number)

                # If Column has more than 1 letter, convert to correct integer
                if len(output) > 1:
                    col_value = ((len(output) - 1) * 26) + output[-1]
                else:
                    col_value = output[0]

                return col_value, row
            # If no cells were found, sheet is empty. Return zero coordinates.
            except:
                return 0, 0


    # Method to translate worksheet titles (the tabs at the bottom of excel)
    def translate_ws_titles(self):
        for i, sheet in enumerate(self.wb.worksheets):
            old_title = sheet.title
            new_title = self.trans.translate(sheet.title)
            
            # If translation failed, reset title to old_title
            if new_title == None:
                new_title = old_title

            # The character '/' in a WS title crashes excel, so need to remove it    
            if "/" in new_title:
                resulting = re.sub("/", " ", new_title)
                self.wb.worksheets[i].title = resulting
                self.ws_titles[old_title] = resulting
                self.log_change(content=f'Changed WS Title {old_title} to {new_title}')

            else:
                self.wb.worksheets[i].title = new_title
                self.ws_titles[old_title] = new_title
                self.log_change(content=f'Changed WS Title {old_title} to {new_title}')


    def loop_thru_worksheet(self, lcol, lrow):
        for row in range(1,(lrow+1)):
            for col in range(1,(lcol+1)):
                char = get_column_letter(col)
                text = str(self.ws[char + str(row)].value)

                # If content starts with '=', check to see if worksheet names are in the excel equation. If yes, use dict translation. if not then pass.
                if text[0] == "=":
                    translated_check = False
                    self.log_change(content=f'Checking if external sheet reference at {char},{row}')
                    for key, value in self.ws_titles.items():
                        if key in text:
                            translation = text.replace(key, ("'" + value + "'"))
                            self.log_change(content=f'{char}{row} was changed to {translation}')
                            self.ws[char + str(row)].value = translation
                            translated_check = True
 
                    if translated_check == False:
                        self.log_change(content=f'{char}{row}was not translated')

                elif text != "None":
                    translation = self.trans.translate(text)
                    self.log_change(content=f'{char}{row} - {translation}')
                    self.ws[char + str(row)].value = translation

                else:
                    self.log_change(content=f'{char}{row} - None')


    def loop_thru_document(self):
        self.translate_ws_titles()
        for i, sheet in enumerate(self.wb.worksheets):
            self.log_change(content=f'Starting to translate: {sheet}')
            print(f'Starting to translate: {sheet}')
            self.ws = self.wb.worksheets[i]
            (col_value, row_value) = self.get_lastcell()
            self.loop_thru_worksheet(lcol=int(col_value), lrow=int(row_value)) 

        self.log_change(content=f'Completed translating {sheet}')      
        print(f'Completed translating {self.name}')

