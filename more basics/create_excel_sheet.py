from openpyxl import Workbook

workbook = Workbook()
curr_sheet = workbook.active

curr_sheet['A1'] = "1"
curr_sheet['A2'] = "Python"
curr_sheet['B1'] = "2"
curr_sheet['B2'] = "Dev!"
curr_sheet['C1'] = "3"
curr_sheet['C2'] = "Society!"

workbook.save(filename="example.xlsx")
