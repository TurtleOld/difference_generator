""" Plain Format """
import json
from gendiff.engine import finding_difference


def format_plain(diff, path=None):
    """
    Функция по переводу словаря данных в строки с указанием тех данных,
    которые изменились.
    :param diff: Переданный словарь.
    :param path: Путь ключей.
    :return: строки с данными
    """
    if path is None:
        path = []

    result = []

    for items in diff:

        status = finding_difference.get_status(items)
        key = finding_difference.get_key(items)
        value = finding_difference.get_value(items)
        child = finding_difference.get_child(items)

        path.append(key)

        if status == finding_difference.VALUE_DELETED:
            result.append("Property '{0}' was removed".format('.'.join(path)))
        if status == finding_difference.VALUE_ADDED:
            result.append("Property '{0}' was added with value: {1}".format(
                '.'.join(path), converted_value(value)
            ))
        if status == finding_difference.VALUE_CHANGED:
            result.append("Property '{0}' was updated. From {1} to {2}".format(
                '.'.join(path), converted_value(value[0]),
                converted_value(value[1])
            ))
        if status == finding_difference.VALUE_NESTED:
            result.append(format_plain(child, path))
        path.pop()
    return '\n'.join(result)


def converted_value(value):
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
