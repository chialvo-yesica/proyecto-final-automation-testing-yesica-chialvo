import json
from pathlib import Path
from config.settings import PROJECT_ROOT

#Carga datos de prueba desde un archivo JSON
def load_test_data_from_json(file_relative_path: str):
    full_file_path = PROJECT_ROOT / file_relative_path
    with open(full_file_path, 'r', encoding="utf-8") as json_file:
        return json.load(json_file)