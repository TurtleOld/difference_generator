""" Function of string representation of data from files """
import json
import yaml


def parsing_string_representation(string):
    if string.startswith('{'):
        result = json.loads(string)
    else:
        result = yaml.safe_load(string)
    return result
