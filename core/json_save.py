import json

def Save_data(data):
 with open('directories_debug.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)