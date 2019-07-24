import pandas as pd
datafile = pd.read_excel(r'data/ASK1563581.xlsx', sheet_name='Sheet1')

print(datafile.head())
