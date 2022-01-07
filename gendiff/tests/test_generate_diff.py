from gendiff import generate_diff

FILE_JSON1 = 'gendiff/tests/fixtures/file1.json'
FILE_JSON2 = 'gendiff/tests/fixtures/file2.json'
FILE_YAML1 = 'gendiff/tests/fixtures/file1.yaml'
FILE_YAML2 = 'gendiff/tests/fixtures/file2.yaml'
FILE_YML1 = 'gendiff/tests/fixtures/file1.yml'
FILE_YML2 = 'gendiff/tests/fixtures/file2.yml'

RECURSION_FILE_JSON1 = 'gendiff/tests/fixtures/file1_recursion.json'
RECURSION_FILE_JSON2 = 'gendiff/tests/fixtures/file2_recursion.json'
RECURSION_FILE_YAML1 = 'gendiff/tests/fixtures/file1_recursion.yaml'
RECURSION_FILE_YAML2 = 'gendiff/tests/fixtures/file2_recursion.yaml'

EXPECTED_RESULT = 'gendiff/tests/fixtures/result.txt'
EXPECTED_RECURSION_RESULT = 'gendiff/tests/fixtures/recursion_result.txt'
EXPECTED_PLAIN_RECURSION_RESULT = \
    'gendiff/tests/fixtures/plain_recursion_result.txt'
EXPECTED_PLAIN_RESULT = 'gendiff/tests/fixtures/plain_result.txt'

diff_json = generate_diff(FILE_JSON1, FILE_JSON2)
diff_yaml = generate_diff(FILE_YAML1, FILE_YAML2)
diff_yml = generate_diff(FILE_YML1, FILE_YML2)
recursion_diff_json = generate_diff(RECURSION_FILE_JSON1, RECURSION_FILE_JSON2)
recursion_diff_yaml = generate_diff(RECURSION_FILE_YAML1, RECURSION_FILE_YAML2)
plain_diff_json1 = generate_diff(FILE_JSON1,
                                 FILE_JSON2,
                                 'plain')
plain_diff_yaml = generate_diff(RECURSION_FILE_YAML1,
                                RECURSION_FILE_YAML2,
                                'plain')
plain_diff_json = generate_diff(RECURSION_FILE_JSON1,
                                RECURSION_FILE_JSON2,
                                'plain')
stylish_diff_yaml = generate_diff(RECURSION_FILE_YAML1,
                                  RECURSION_FILE_YAML2,
                                  'stylish')
stylish_diff_json = generate_diff(RECURSION_FILE_JSON1,
                                  RECURSION_FILE_JSON2,
                                  'stylish')


def test_generate_diff():
    assert diff_json == open(EXPECTED_RESULT, 'r').read()
    assert diff_yaml == open(EXPECTED_RESULT, 'r').read()
    assert diff_yml == open(EXPECTED_RESULT, 'r').read()
    assert recursion_diff_json == open(EXPECTED_RECURSION_RESULT, 'r').read()
    assert recursion_diff_yaml == open(EXPECTED_RECURSION_RESULT, 'r').read()


def test_plain_format_diff():
    assert plain_diff_yaml == open(EXPECTED_PLAIN_RECURSION_RESULT, 'r').read()
    assert plain_diff_json == open(EXPECTED_PLAIN_RECURSION_RESULT, 'r').read()
    assert plain_diff_json1 == open(EXPECTED_PLAIN_RESULT, 'r').read()


def test_stylish_diff():
    assert stylish_diff_yaml == open(EXPECTED_RECURSION_RESULT, 'r').read()
    assert stylish_diff_json == open(EXPECTED_RECURSION_RESULT, 'r').read()
