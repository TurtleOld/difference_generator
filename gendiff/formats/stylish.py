""" Stylish Format """
from gendiff.engine import finding_difference

COUNT_INDENT = 4
SYMBOL_INDENT = ' '

TEMPLATE_STRING = '{indent}{symbol} {key}: {value}'

SYMBOL_ADDED = '+'
SYMBOL_DELETED = '-'
SYMBOL_UNCHANGED = ' '


def get_indent(depth: int) -> tuple:
    """
    Функция по определению начального и конечного отступа.
    """
    open_indent = SYMBOL_INDENT * (COUNT_INDENT * depth - 2)
    close_indent = SYMBOL_INDENT * (COUNT_INDENT * (depth - 1))

    return open_indent, close_indent


def get_value(item, depth) -> str:
    """ Получение значения. """
    result = []

    open_indent, close_indent = get_indent(depth)

    if isinstance(item, dict):
        result.append('{')
        for key, value in item.items():
            result.append('{indent}{symbol} {key}: {value}'.format(
                indent=open_indent, symbol=SYMBOL_UNCHANGED,
                key=key, value=get_value(value, depth + 1)
            ))

        result.append(close_indent + '}')
    elif isinstance(item, bool):
        result.append(str(item).lower())
    elif item is None:
        result.append('null')
    else:
        result.append(str(item))
    return '\n'.join(result)


def get_format_stylish(tree: list, depth=1) -> str:
    """ Построение формата stylish. """
    result_data = ['{']
    open_indent, close_indent = get_indent(depth)

    for item in tree:
        type_vertex = item['type']
        key = item['key']
        value = item['value1'], item['value2']
        nested = item['nested']

        if type_vertex == finding_difference.VALUE_DELETED:
            result_data.append('{indent}{symbol} {key}: {value}'.format(
                indent=open_indent, symbol=SYMBOL_DELETED, key=key,
                value=get_value(value[0], depth + 1)
            ))

        elif type_vertex == finding_difference.VALUE_ADDED:
            result_data.append('{indent}{symbol} {key}: {value}'.format(
                indent=open_indent, symbol=SYMBOL_ADDED, key=key,
                value=get_value(value[0], depth + 1)
            ))

        elif type_vertex == finding_difference.VALUE_UNCHANGED:
            result_data.append('{indent}{symbol} {key}: {value}'.format(
                indent=open_indent, symbol=SYMBOL_UNCHANGED, key=key,
                value=get_value(value[0], depth + 1)
            ))

        elif type_vertex == finding_difference.VALUE_NESTED:
            result_data.append('{indent}{symbol} {key}: {value}'.format(
                indent=open_indent, symbol=SYMBOL_UNCHANGED, key=key,
                value=get_format_stylish(nested, depth + 1)
            ))

        else:
            result_data.append('{indent}{symbol} {key}: {value}'.format(
                indent=open_indent, symbol=SYMBOL_DELETED, key=key,
                value=get_value(value[0], depth + 1)
            ))
            result_data.append('{indent}{symbol} {key}: {value}'.format(
                indent=open_indent, symbol=SYMBOL_ADDED, key=key,
                value=get_value(value[1], depth + 1)
            ))

    result_data.append(close_indent + '}')
    return '\n'.join(result_data)
