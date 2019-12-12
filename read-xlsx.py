import pandas as pd
from mako import exceptions

from column_wise_not_null import create_master_file
from column_wise_not_null import generate_liquibase_files
from model import Column
from model import Table

data = pd.read_excel('./liquibase-schema.xlsx')
columns = ['name', 'type', 'length', 'not null',
           'unique', 'composite', 'default']
dataFrame = pd.DataFrame(data, columns=columns)

tableName = ''
columns = []
isOk = False
tableList = []

for i, r in dataFrame.iterrows():
    name = r['name']
    dataType = r['type']
    notNull = r['not null']
    unique = r['unique']
    composite = r['composite']
    default = r['default']

    if pd.isna(name):
        continue

    if dataType == 'TABLE':
        if isOk:
            table = Table(name=tableName, columns=columns)
            tableList.append(table)
        isOk = True
        columns = []
        tableName = name
    elif dataType == 'composite':  # todo: need to handle composite key
        continue
    elif notNull != 'yes':
        continue
    else:
        columns.append(Column(name=name, type=dataType, defaultValue=default))

table = Table(name=tableName, columns=columns)
tableList.append(table)

for t in tableList:
    try:
        create_master_file()
        generate_liquibase_files(t)
        print('~~ File Generation Successful! ~~')
    except:
        print(exceptions.text_error_template().render())
