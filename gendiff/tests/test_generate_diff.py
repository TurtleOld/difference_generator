from gendiff import generate_diff
from fixtures.result import result


file1 = 'file1.json'
file2 = 'file2.json'


def test_generate_diff():
    assert type(generate_diff(file1, file2)) == str
    assert generate_diff(file1, file2) == result
