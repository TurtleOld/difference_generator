import json


def generate_diff(filepath1, filepath2):
    result = ['{']
    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))
    keys = sorted(file1.keys() | file2.keys())
    for key in keys:
        return key
