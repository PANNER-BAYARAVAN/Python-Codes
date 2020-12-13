import pandas as pd

df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

writer.save()