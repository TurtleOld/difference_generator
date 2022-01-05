import json
import yaml

TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')


def determining_file_format(file_path):
    if file_path.endswith(TYPE_JSON):
        format_file = json.load(open(file_path))

    if file_path.endswith(TYPE_YML_OR_YAML):
        format_file = yaml.safe_load(open(file_path))

    return format_file


def finding_difference(file_path1, file_path2):
    tuple_value1 = {(key, value) for key, value in file_path1.items()}
    tuple_value2 = {(key, value) for key, value in file_path2.items()}
    list_tuple_values = sorted(list(tuple_value1 | tuple_value2))
    list_result = ['{']

    for key, _ in list_tuple_values:
        if key in file_path1.keys() and key in file_path2.keys():
            if file_path1[key] == file_path2[key]:
                list_result.append('   {0}: {1}'.format(key, file_path1[key]))
            else:
                list_result.append(' - {0}: {1}'.format(key, file_path1[key]))
                list_result.append(' + {0}: {1}'.format(key, file_path2[key]))
        else:
            if key in file_path1.keys():
                list_result.append(' - {0}: {1}'.format(key, file_path1[key]))
            else:
                list_result.append(' + {0}: {1}'.format(key, file_path2[key]))

    list_result.append('}')
    result = sorted(set(list_result),
                    key=lambda index: list_result.index(index))
    new_result = '\n'.join(result)
    return new_result
