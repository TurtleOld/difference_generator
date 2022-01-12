""" Function of string representation of data from files """
import json
import yaml


def parsing_file_content(content):
    if content.startswith('{') or content.startswith('['):
        result = json.loads(content)
    else:
        result = yaml.safe_load(content)
    return result
