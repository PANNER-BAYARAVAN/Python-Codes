import pandas as pd

df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

writer = pd.ExcelWriter('pandas_conditional.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

workbook  = writer.book
worksheet = writer.sheets['Sheet1']

worksheet.conditional_format('B2:B8', {'type': '3_color_scale'})

writer.save()