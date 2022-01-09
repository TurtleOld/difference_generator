from gendiff import generate_diff

FILE_JSON1 = 'tests/fixtures/file1.json'
FILE_JSON2 = 'tests/fixtures/file2.json'
FILE_YAML1 = 'tests/fixtures/file1.yaml'
FILE_YAML2 = 'tests/fixtures/file2.yaml'
FILE_YML1 = 'tests/fixtures/file1.yml'
FILE_YML2 = 'tests/fixtures/file2.yml'

RECURSION_FILE_JSON1 = 'tests/fixtures/file1_recursion.json'
RECURSION_FILE_JSON2 = 'tests/fixtures/file2_recursion.json'
RECURSION_FILE_YAML1 = 'tests/fixtures/file1_recursion.yaml'
RECURSION_FILE_YAML2 = 'tests/fixtures/file2_recursion.yaml'

EXPECTED_RESULT = 'tests/fixtures/result.txt'
EXPECTED_RECURSION_RESULT = 'tests/fixtures/recursion_result.txt'

EXPECTED_PLAIN_RECURSION_RESULT = \
    'tests/fixtures/plain_recursion_result.txt'
EXPECTED_PLAIN_RESULT = 'tests/fixtures/plain_result.txt'

EXPECTED_JSON_RESULT = 'tests/fixtures/json_result_json.txt'
EXPECTED_RECURSION_JSON_RESULT = \
    'tests/fixtures/json_recursion_result_json.txt'

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
json_diff_json = generate_diff(FILE_JSON1,
                               FILE_JSON2,
                               'json')
json_recursion_diff_json = generate_diff(RECURSION_FILE_JSON1,
                                         RECURSION_FILE_JSON2,
                                         'json')


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


def test_json_diff():
    assert json_diff_json == open(EXPECTED_JSON_RESULT, 'r').read()
    assert json_recursion_diff_json == open(
        EXPECTED_RECURSION_JSON_RESULT, 'r').read()
