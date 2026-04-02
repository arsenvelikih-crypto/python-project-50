import json


# форматирование в виде JSON
def format_json(diff):
    return json.dumps(diff, indent=4, ensure_ascii=False)
