from gendiff import generate_diff

file1 = 'file1.json'
file2 = 'file2.json'


def test_generate_diff():
    assert type(generate_diff(file1, file2)) == str
    assert generate_diff(file1, file2) == '{\n - follow: False\n   ' \
                                          'host: hexlet.io\n' \
                                          ' - proxy: 123.234.53.22\n' \
                                          ' - timeout: 50\n' \
                                          ' + timeout: 20\n + verbose: True\n}'
