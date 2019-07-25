import pandas as pd
datafile = pd.read_excel(r'data/ASK1563581.xlsx', sheet_name='Sheet1')

#print(datafile.head())


#print(datafile.groupby('DBName').count())
#print(datafile.duplicated('EventName').count())

grouped = datafile['EventName'].groupby(datafile['DBName'])
listoflists = []
for name, group in grouped:
    name = []
    for i in group:
        name.append(i)
    listoflists.append(name)
#print(listoflists)
print(len(set.intersection(*[set(list) for list in listoflists])))
print(set.intersection(*[set(list) for list in listoflists]))
