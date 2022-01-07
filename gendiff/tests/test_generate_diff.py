from gendiff import generate_diff
from gendiff.formats import stylish, plain

file_json1 = 'gendiff/tests/fixtures/file1.json'
file_json2 = 'gendiff/tests/fixtures/file2.json'
file_yaml1 = 'gendiff/tests/fixtures/file1.yaml'
file_yaml2 = 'gendiff/tests/fixtures/file2.yaml'
file_yml1 = 'gendiff/tests/fixtures/file1.yml'
file_yml2 = 'gendiff/tests/fixtures/file2.yml'

recursion_file_json1 = 'gendiff/tests/fixtures/file1_recursion.json'
recursion_file_json2 = 'gendiff/tests/fixtures/file2_recursion.json'
recursion_file_yaml1 = 'gendiff/tests/fixtures/file1_recursion.yaml'
recursion_file_yaml2 = 'gendiff/tests/fixtures/file2_recursion.yaml'

expected_result = 'gendiff/tests/fixtures/result.txt'
expected_recursion_result = 'gendiff/tests/fixtures/recursion_result.txt'
expected_plain_result = 'gendiff/tests/fixtures/plain_result.txt'

diff_json = generate_diff(file_json1, file_json2)
diff_yaml = generate_diff(file_yaml1, file_yaml2)
diff_yml = generate_diff(file_yml1, file_yml2)
recursion_diff_json = generate_diff(recursion_file_json1, recursion_file_json2)
recursion_diff_yaml = generate_diff(recursion_file_yaml1, recursion_file_yaml2)
plain_diff = generate_diff(recursion_file_yaml1, recursion_file_yaml2, 'plain')
stylish_diff = generate_diff(recursion_file_yaml1,
                             recursion_file_yaml2,
                             'stylish')


def test_generate_diff():
    assert diff_json == open(expected_result, 'r').read()
    assert diff_yaml == open(expected_result, 'r').read()
    assert diff_yml == open(expected_result, 'r').read()
    assert recursion_diff_json == open(expected_recursion_result, 'r').read()
    assert recursion_diff_yaml == open(expected_recursion_result, 'r').read()


def test_plain_format_diff():
    assert plain_diff == open(expected_plain_result, 'r').read()


def test_stylish_diff():
    assert stylish_diff == open(expected_recursion_result, 'r').read()
