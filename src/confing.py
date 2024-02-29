import os
import json

dir_root = os.path.dirname(__file__)
dir_path_json = os.path.join(dir_root, 'file', 'operations.json')

with open(dir_path_json, encoding='UTF8') as f:
    file_content = f.read()
    operations_json = json.loads(file_content)
