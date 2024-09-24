import json

def SerializzaJson(data, file_path) -> bool:
    try:
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(data, indent=True))
        return True
    except:
        return False

def DeserializzaJson(file_path) -> dict:
    with open(file_path, mode='r', encoding='utf-8') as f:
        output:dict = json.load(f)
    return output

mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}
SerializzaJson
print(SerializzaJson(mydict_1, 'placeholder.json'))
print(DeserializzaJson('placeholder.json'))