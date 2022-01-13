""" Tests """
import pytest

from gendiff import generate_diff


@pytest.mark.parametrize('file1, file2, formats, expected', [
    (
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        'stylish',
        'tests/fixtures/result.txt'
    ),
    (
        'tests/fixtures/file1.yaml',
        'tests/fixtures/file2.yaml',
        'stylish',
        'tests/fixtures/result.txt'
    ),
    (
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml',
        'stylish',
        'tests/fixtures/result.txt'
    ),
    (
        'tests/fixtures/file1_recursion.json',
        'tests/fixtures/file2_recursion.json',
        'stylish',
        'tests/fixtures/recursion_result.txt'
    ),
    (
        'tests/fixtures/file1_recursion.yaml',
        'tests/fixtures/file2_recursion.yaml',
        'stylish',
        'tests/fixtures/recursion_result.txt'
    ),
    (
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        'plain',
        'tests/fixtures/plain_result.txt'
    ),
    (
        'tests/fixtures/file1_recursion.json',
        'tests/fixtures/file2_recursion.json',
        'plain',
        'tests/fixtures/plain_recursion_result.txt'
    ),
    (
        'tests/fixtures/file1_recursion.yaml',
        'tests/fixtures/file2_recursion.yaml',
        'plain',
        'tests/fixtures/plain_recursion_result.txt'
    ),
    (
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        'json',
        'tests/fixtures/json_result.txt'
    ),
    (
        'tests/fixtures/file1_recursion.json',
        'tests/fixtures/file2_recursion.json',
        'json',
        'tests/fixtures/json_recursion_result.txt'
    ),
    (
        'tests/fixtures/file1_recursion.yaml',
        'tests/fixtures/file2_recursion.yaml',
        'json',
        'tests/fixtures/json_recursion_result.txt'
    ),
])
def test_difference_generator(file1, file2, formats, expected):
    with open(expected, 'r') as file:
        result = file.read()
    assert generate_diff(file1, file2, formats) == result
