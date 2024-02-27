import os
import json

dir_root = os.path.dirname(__file__)
dir_json = os.path.join(dir_root, 'file', 'operations.json')

print(dir_json)

#
#
# dir_json = os.path.join(root, "operations.json")
#
#
# with open(dir_json, encoding='UTF8') as f:
#     file_content = f.read()
#     operations_json = json.loads(file_content)

