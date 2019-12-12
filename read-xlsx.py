import pandas as pd

# from model import Table
# from model import Column

data = pd.read_excel('/home/eatl/python/liquibase-schema.xlsx')
columns = ['name', 'type', 'length', 'not null',
           'unique', 'composite', 'default']
dataFrame = pd.DataFrame(data, columns=columns)

for i, r in dataFrame.iterrows():
    name = r['name']
    dataType = r['type']
    notNull = r['not null']
    unique = r['unique']
    composite = r['composite']
    # print(name, ' ', dataType, ' ', notNull, ' ', unique, ' ', composite)
    if dataType == 'TABLE':
        print('table data: ', name)
