import json


def generate_diff(filepath1, filepath2):
    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))
    tuple_value1 = {(key, value) for key, value in file1.items()}
    tuple_value2 = {(key, value) for key, value in file2.items()}
    list_tuple_values = sorted(list(tuple_value1 | tuple_value2))
    list_result = ['{']

    for key, _ in list_tuple_values:
        if key in file1.keys() and key in file2.keys():
            if file1[key] == file2[key]:
                list_result.append('   {0}: {1}'.format(key, file1[key]))
            else:
                list_result.append(' - {0}: {1}'.format(key, file1[key]))
                list_result.append(' + {0}: {1}'.format(key, file2[key]))
        else:
            if key in file1.keys():
                list_result.append(' - {0}: {1}'.format(key, file1[key]))
            else:
                list_result.append(' + {0}: {1}'.format(key, file2[key]))

    list_result.append('}')
    result = sorted(set(list_result),
                    key=lambda index: list_result.index(index))
    new_result = '\n'.join(result)
    return new_result
