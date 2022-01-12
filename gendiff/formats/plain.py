""" Plain Format """
import json
from gendiff.engine import finding_difference


def get_format_plain(tree, path=None):
    """
    Функция по переводу словаря данных в строки с указанием тех данных,
    которые изменились.
    :param tree: Переданный словарь.
    :param path: Путь ключей.
    :return: строки с данными
    """
    if path is None:
        path = []

    result = []

    for items in tree:

        type_vertex = items['type']
        key = items['key']
        value = items['value1'], items['value2']
        nested = items['nested']

        path.append(key)

        if type_vertex == finding_difference.VALUE_DELETED:
            result.append("Property '{0}' was removed".format('.'.join(path)))
        if type_vertex == finding_difference.VALUE_ADDED:
            result.append("Property '{0}' was added with value: {1}".format(
                '.'.join(path), get_converted_value(value)
            ))
        if type_vertex == finding_difference.VALUE_CHANGED:
            result.append("Property '{0}' was updated. From {1} to {2}".format(
                '.'.join(path), get_converted_value(value[0]),
                get_converted_value(value[1])
            ))
        if type_vertex == finding_difference.VALUE_NESTED:
            result.append(get_format_plain(nested, path))
        path.pop()
    return '\n'.join(result)


def get_converted_value(value):
    """
    Функция по конвертации данных.
    :param value: Значение словаря.
    :return: нужный формат.
    """
    if type(value) is tuple:
        if type(value[0]) is str:
            collecting = "'{}'".format(value[0])
        elif type(value[0]) is dict:
            collecting = '[complex value]'
        else:
            collecting = json.dumps(value[0])
    elif type(value) is int:
        collecting = '{0}'.format(value)
    elif type(value) is str:
        collecting = "'{0}'".format(value)
    elif type(value) is dict:
        collecting = '[complex value]'
    else:
        collecting = json.dumps(value)

    result = collecting

    return result
