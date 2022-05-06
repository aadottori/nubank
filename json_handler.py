import json


def create_json(function, user):
    with open(f"results/{user}/{function.__name__}.json", 'w', encoding='utf-8') as f:
        json.dump(function(), f, ensure_ascii=False, indent=4)