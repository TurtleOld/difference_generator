import json
from gendiff import finding_difference


def format_plain(diff, path=None):
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
        if status == finding_difference.VALUE_CHILD:
            result.append(format_plain(child, path))
        path.pop()
    return '\n'.join(result)


def converted_value(value):
    if type(value) is str:
        return "'{}'".format(value)
    if type(value) is tuple:
        if type(value[0]) is str:
            return "'{}'".format(value[0])
        if type(value[0]) is dict:
            return '[complex value]'
        if value[0] in [True, False, None]:
            return json.dumps(value[0])
    if type(value) is dict:
        return '[complex value]'
    if value in [True, False, None]:
        return json.dumps(value)
