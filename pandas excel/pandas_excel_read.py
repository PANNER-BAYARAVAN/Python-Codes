import pandas as pd

data = pd.read_excel (r'C:\Users\DrLallan\Desktop\Product List.xlsx') 
df = pd.DataFrame(data, columns= ['Product'])
print (df)