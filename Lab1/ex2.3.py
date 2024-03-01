import json

with open("large-file.json", "r", encoding="utf-8") as json_file: #Used Copilot for encoding part
    data = json.load(json_file)

for datas in data:
    datas['size'] = 35
    
with open("output.2.3.json", "w") as file:
    json.dump(data[::-1], file, indent=2)