from .extensions.excel import Workbook


class App():
    def __init__(self) -> None:
        self.project_name = 'input' # Name the input folder this as well
        self.template_name = 'blank.xlsx'
        self.content_list = []


    def excel_loop(self) -> None:
            template = Workbook(self.template_name, self.project_name, self.content_list)





# Load Template
# Get formatting from template
# - Font, Fill, Border, Alignment, Hyperlink (KEEP RELATIVE)
#
# 
# 
# 
#  
