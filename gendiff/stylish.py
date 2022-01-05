from gendiff import finding_difference

COUNT_INDENT = 4
SYMBOL_INDENT = ' '

TEMPLATE_STRING = '{indent}{symbol} {key}: {value}'

SYMBOL_ADDED = '+'
SYMBOL_DELETED = '-'
SYMBOL_UNCHANGED = ' '


def get_indent(depth):
    open_indent = SYMBOL_INDENT * (COUNT_INDENT * depth - 2)
    close_indent = SYMBOL_INDENT * (COUNT_INDENT * (depth - 1))

    return open_indent, close_indent


def get_string(indent, symbol, key, value):
    return TEMPLATE_STRING.format(indent=indent, symbol=symbol, key=key,
                                  value=value)


def get_value(item, depth):
    result = []

    open_indent, close_indent = get_indent(depth)

    if isinstance(item, dict):
        result.append('{')
        for key, value in item.items():
            result.append(get_string(open_indent,
                                     SYMBOL_UNCHANGED,
                                     key,
                                     get_value(value, depth + 1)))
        result.append(close_indent + '}')
    elif isinstance(item, bool):
        result.append(str(item).lower())
    elif item is None:
        result.append('null')
    else:
        result.append(str(item))
    return '\n'.join(result)


def get_stylish(tree, depth=1):
    result_data = ['{']
    open_indent, close_indent = get_indent(depth)

    for item in tree:
        status = finding_difference.get_status(item)
        key = finding_difference.get_key(item)
        value = finding_difference.get_value(item)
        child = finding_difference.get_child(item)

        if status == finding_difference.VALUE_DELETED:
            result_data.append(get_string(open_indent,
                                          SYMBOL_DELETED,
                                          key,
                                          get_value(value[0], depth + 1)))

        elif status == finding_difference.VALUE_ADDED:
            result_data.append(get_string(open_indent,
                                          SYMBOL_ADDED,
                                          key,
                                          get_value(value[0], depth + 1)))

        elif status == finding_difference.VALUE_UNCHANGED:
            result_data.append(get_string(open_indent,
                                          SYMBOL_UNCHANGED,
                                          key,
                                          get_value(value[0], depth + 1)))

        elif status == finding_difference.VALUE_CHILD:
            result_data.append(get_string(open_indent,
                                          SYMBOL_UNCHANGED,
                                          key,
                                          get_stylish(child, depth + 1)))

        else:
            result_data.append(get_string(open_indent,
                                          SYMBOL_DELETED,
                                          key,
                                          get_value(value[0], depth + 1)))
            result_data.append(get_string(open_indent,
                                          SYMBOL_ADDED,
                                          key,
                                          get_value(value[1], depth + 1)))

    result_data.append(close_indent + '}')
    return '\n'.join(result_data)
