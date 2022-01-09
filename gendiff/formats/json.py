import json


def format_json(data):
    """ Функция по созданию итоговых данных в формате JSON. """
    return json.dumps(data, indent=2)
