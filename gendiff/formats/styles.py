from gendiff.formats import stylish, plain, json


FORMATS = {
    'stylish': stylish.format_stylish,
    'plain': plain.format_plain,
    'json': json.format_json
}
