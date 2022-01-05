from gendiff import generate_diff
from fixtures.result import result


file_json1 = 'gendiff/tests/fixtures/file1.json'
file_json2 = 'gendiff/tests/fixtures/file2.json'
file_yaml1 = 'gendiff/tests/fixtures/file1.yaml'
file_yaml2 = 'gendiff/tests/fixtures/file2.yaml'


def test_generate_diff():
    assert type(generate_diff(file_json1, file_json2)) == str
    assert generate_diff(file_json1, file_json2) == result
    assert generate_diff(file_yaml1, file_yaml2) == result
