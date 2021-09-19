import json


def create_json(function):
    with open("results/{}.json".format(function.__name__), 'w', encoding='utf-8') as f:
        json.dump(function(), f, ensure_ascii=False, indent=4)