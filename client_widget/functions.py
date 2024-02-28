import json
from confing import dir_path_json


with open(dir_path_json, encoding='UTF8') as f:
    file_content = f.read()
    operations_json = json.loads(file_content)
