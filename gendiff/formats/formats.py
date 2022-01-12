""" Formats dictionary """
from gendiff.formats import stylish, plain, json


FORMATS = {
    'stylish': stylish.get_format_stylish,
    'plain': plain.get_format_plain,
    'json': json.format_json
}


FORMAT_FILES = {
    'json': '.json',
    'yaml_yml': ('.yml', '.yaml')
}
