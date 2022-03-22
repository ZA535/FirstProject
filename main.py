import json
from msilib.schema import File

default_connect_location = '127.0.0.1'
from test_file import Box


def getConnection(location=None):
    loc = default_connect_location
    if location:
        loc = location
    return 'Connected:' + loc

# "192.168.10.1"
print(getConnection("198.168.15.1"))
# file_data = ''
# with open('names.txt','r') as nf:
#     file_data = nf.read()
# lines = file_data.split('\n')
# user_data = []
# for line in lines:
#     d = line.split(',')
#     user_data.append({
#         'name':d[0],
#         'age':d[1],
#         'year':d[2]
#     })
# json_data = json.dumps(user_data)
# with open('names.json','w') as nf:
#     nf.write(json_data)
#
# dict_js = None
with open('names.json','r') as nf:
    jf = nf.read()
    dict_js = json.loads(jf)

# print(dict_js[0])
