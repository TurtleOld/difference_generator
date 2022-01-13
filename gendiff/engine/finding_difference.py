""" Creating representation difference. """

VALUE_DELETED = 'deleted'
VALUE_ADDED = 'added'
VALUE_CHANGED = 'changed'
VALUE_UNCHANGED = 'unchanged'
VALUE_NESTED = 'nested'


def create_tree_vertex(dictionary_1: dict, dictionary_2: dict) -> list:
    """
    Функция создания разницы между данными двух файлов.
    :param dictionary_1: Словарь.
    :param dictionary_2: Словарь.
    :return: Формирует вершину дерева.
    """
    keys1 = dictionary_1.keys()
    keys2 = dictionary_2.keys()
    keys = keys1 | keys2
    list_result = []

    for dict_key in sorted(keys):
        if dict_key not in dictionary_1:
            children = {'type': VALUE_ADDED, 'key': dict_key,
                        'value1': dictionary_2[dict_key], 'value2': None,
                        'nested': None
                        }

        elif dict_key not in dictionary_2:
            children = {'type': VALUE_DELETED, 'key': dict_key,
                        'value1': dictionary_1[dict_key], 'value2': None,
                        'nested': None
                        }

        elif dictionary_1[dict_key] == dictionary_2[dict_key]:
            children = {'type': VALUE_UNCHANGED, 'key': dict_key,
                        'value1': dictionary_1[dict_key], 'value2': None,
                        'nested': None
                        }

        elif isinstance(dictionary_1[dict_key], dict) and isinstance(
                dictionary_2[dict_key], dict):
            children = {'type': VALUE_NESTED, 'key': dict_key,
                        'value1': None, 'value2': None,
                        'nested': create_tree_vertex(dictionary_1[dict_key],
                                                     dictionary_2[dict_key]
                                                     )}
        else:
            children = {'type': VALUE_CHANGED, 'key': dict_key,
                        'value1': dictionary_1[dict_key],
                        'value2': dictionary_2[dict_key], 'nested': None
                        }

        list_result.append(children)

    return list_result
