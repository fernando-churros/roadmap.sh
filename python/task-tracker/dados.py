import json

file_json = 'dados.json'

def all_tasks() -> list:
    try:
        with open(file_json, "r", encoding="utf-8") as f:
            x = json.load(f)

    except FileNotFoundError:
        with open(file_json, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        x = []

    return x
