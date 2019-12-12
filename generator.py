import time
from mako import exceptions
from datetime import datetime
from mako.template import Template

DELAY_SEC = 1

tableList = [
    'employee',
    'employee_posting',
    'permission',
    'permission_parent',
    'role',
    'role_action',
    'service_action',
    'user_temp',
]

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%Y%m%d%H%M%S")
    return current_time

def create_not_null_xml(xmlFile, content):
    path = '/home/eatl/python/liquibase-out/'
    f = open(path + xmlFile, "w")
    f.write(content)
    f.close()

def get_table_name(dbTable):
    parts = dbTable.split('_')
    parts = [x.title() for x in parts]
    return ''.join(parts)

def create_master_file():
    path = '/home/eatl/python/liquibase-out/master/'
    f = open(path + 'master.xml', "w")
    f.write('')
    f.close()

def generate_master_xml(xmlFile):
    content = '<include file="config/liquibase/changelog/' + xmlFile + '" relativeToChangelogFile="false"/>\n'
    
    path = '/home/eatl/python/liquibase-out/master/'
    f = open(path + 'master.xml', "a")
    f.write(content)
    f.close()

def generate_liquibase_files(table_name):
    curr_time = get_current_time()
    dictionary = {
        'current_time': curr_time,
        'action': 'AddNotNull',
        'author_name': 'roy',
        'table_name': table_name,
    }

    template = Template(filename='/home/eatl/python/not-null-liquibase-template.xml')
    xmlFile = curr_time + '-add-not_null-constraint-on-' + get_table_name(table_name) + '.xml'
    content = template.render(**dictionary)
    create_not_null_xml(xmlFile, content)
    print('-> Generated: ' + xmlFile)
    generate_master_xml(xmlFile)
    time.sleep(DELAY_SEC)

try:
    create_master_file()
    for table_name in tableList:
        generate_liquibase_files(table_name)
    print('~~ File Generation Successful! ~~')
except:
        print(exceptions.text_error_template().render())
