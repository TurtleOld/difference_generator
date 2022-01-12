""" JSON Format """
import json


def get_format_json(data):
    """ Функция по созданию итоговых данных в формате JSON. """
    return json.dumps(data, indent=2)
