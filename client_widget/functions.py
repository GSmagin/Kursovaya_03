import json
from confing import dir_json

with open(dir_json, encoding='UTF8') as f:
    file_content = f.read()
    operations_json = json.loads(file_content)


