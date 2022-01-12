""" Creating representation difference. """
VALUE_DELETED = 'deleted'
VALUE_ADDED = 'added'
VALUE_CHANGED = 'changed'
VALUE_UNCHANGED = 'unchanged'
VALUE_NESTED = 'nested'


def create_difference_segment(vertex_type, key, value1, value2=None,
                              nested=None):
    """
    Функция-аккумулятор ключей.
    """
    collected_data = {
        'type': vertex_type,
        'key': key,
        'value1': value1,
        'value2': value2,
        'nested': nested
    }
    return collected_data


def create_tree_vertex(dictionary_1: dict, dictionary_2: dict):
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
            children = create_difference_segment(VALUE_ADDED,
                                                 dict_key,
                                                 dictionary_2[dict_key])
        elif dict_key not in dictionary_2:
            children = create_difference_segment(VALUE_DELETED,
                                                 dict_key,
                                                 dictionary_1[dict_key])
        elif dictionary_1[dict_key] == dictionary_2[dict_key]:
            children = create_difference_segment(VALUE_UNCHANGED,
                                                 dict_key,
                                                 dictionary_1[dict_key])
        elif isinstance(dictionary_1[dict_key], dict) and isinstance(
                dictionary_2[dict_key], dict):
            children = create_difference_segment(
                VALUE_NESTED,
                dict_key,
                value1=None,
                nested=create_tree_vertex(dictionary_1[dict_key],
                                          dictionary_2[dict_key]
                                          )
            )
        else:
            children = create_difference_segment(VALUE_CHANGED,
                                                 dict_key,
                                                 value1=dictionary_1[
                                                     dict_key],
                                                 value2=dictionary_2[
                                                     dict_key])
        list_result.append(children)

    return list_result
