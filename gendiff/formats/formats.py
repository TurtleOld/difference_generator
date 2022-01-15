""" Formats dictionary """
from gendiff.formats import stylish, plain, json


FORMATS = {
    'stylish': stylish.render,
    'plain': plain.render,
    'json': json.get_format_json
}


FORMAT_FILES = {
    'json': '.json',
    'yaml_yml': ('.yml', '.yaml')
}
