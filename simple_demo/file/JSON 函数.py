# json.dumps 将 Python 对象编码成 JSON 字符串
# json.loads 将已编码的 JSON 字符串解码为 Python 对象

import json

data = {'number': 6, 'name': 'Pythontab'}

jsonData = json.dumps(data)
print(jsonData)  # {"number": 6, "name": "Pythontab"}


jsonData = '{"number": 6, "name": "pythontab"}'
strJson = json.loads(jsonData)
print(strJson)  # {'number': 6, 'name': 'pythontab'}









