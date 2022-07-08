import json
from typing import Dict

from manager.getData import create_events_dict


def get_events(num: int) -> None:
    try:
        items = create_events_dict(num)
        file_name = "items.json"
        with open("items.json", mode="w") as f:
            json.dump(items, f, ensure_ascii=False)
        return file_name
    except:
        return False



def load_json(file) -> Dict:
    with open(file) as f:
        data = json.load(f)
    return data