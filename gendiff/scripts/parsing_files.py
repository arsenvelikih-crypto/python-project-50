import json
import os

import yaml


# чтение и парсинг файлов
def parse(file_path):
    ext = os.path.splitext(file_path)[1]
    with open(file_path, 'r') as f:
        if ext == '.json':
            return json.load(f)
        elif ext in ('.yml', '.yaml'):
            return yaml.safe_load(f)
        else:
            raise ValueError(f'Unsupported file format: {ext}')