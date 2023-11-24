import pandas as pd

excel_file = r'D:\nghia\python\python\TT\BT5\file\sheet.xlsx'

sheet_name = "student"

df = pd.read_excel(excel_file, sheet_name=sheet_name)

selected_data = df 

print(selected_data)