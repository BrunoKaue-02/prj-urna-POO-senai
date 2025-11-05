import json
import os

def apagar_db_json(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
