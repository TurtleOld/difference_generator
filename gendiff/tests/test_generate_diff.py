from gendiff import generate_diff

plain_file_json1 = 'gendiff/tests/fixtures/file1.json'
plain_file_json2 = 'gendiff/tests/fixtures/file2.json'
plain_file_yaml1 = 'gendiff/tests/fixtures/file1.yaml'
plain_file_yaml2 = 'gendiff/tests/fixtures/file2.yaml'
plain_file_yml1 = 'gendiff/tests/fixtures/file1.yml'
plain_file_yml2 = 'gendiff/tests/fixtures/file2.yml'

recursion_file_json1 = 'gendiff/tests/fixtures/file1_recursion.json'
recursion_file_json2 = 'gendiff/tests/fixtures/file2_recursion.json'
recursion_file_yaml1 = 'gendiff/tests/fixtures/file1_recursion.yaml'
recursion_file_yaml2 = 'gendiff/tests/fixtures/file2_recursion.yaml'

expected_plain_result = 'gendiff/tests/fixtures/plain_result.txt'
expected_recursion_result = 'gendiff/tests/fixtures/recursion_result.txt'

plain_diff_json = generate_diff(plain_file_json1, plain_file_json2)
plain_diff_yaml = generate_diff(plain_file_yaml1, plain_file_yaml2)
plain_diff_yml = generate_diff(plain_file_yml1, plain_file_yml2)
recursion_diff_json = generate_diff(recursion_file_json1, recursion_file_json2)
recursion_diff_yaml = generate_diff(recursion_file_yaml1, recursion_file_yaml2)


def test_generate_diff():
    assert plain_diff_json == open(expected_plain_result, 'r').read()
    assert plain_diff_yaml == open(expected_plain_result, 'r').read()
    assert plain_diff_yml == open(expected_plain_result, 'r').read()
    assert recursion_diff_json == open(expected_recursion_result, 'r').read()
    assert recursion_diff_yaml == open(expected_recursion_result, 'r').read()
