class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns


class Column:
    def __init__(self, name, type, defaultValue):
        self.name = name
        self.type = type
        self.defaultValue = defaultValue


# columns = []
# columns.append(Column(name='department_id', type='long', defaultValue=''))
# columns.append(Column(name='designation_id', type='long', defaultValue=''))
# columns.append(Column(name='employee_id', type='long', defaultValue=''))

# table = Table('employee', columns)
