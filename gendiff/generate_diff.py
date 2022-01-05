from gendiff.finding_difference import determining_file_format,\
    creating_difference
from gendiff.stylish import get_stylish


def generate_diff(file_path1, file_path2, style=get_stylish):
    file1 = determining_file_format(file_path1)
    file2 = determining_file_format(file_path2)
    return style(creating_difference(file1, file2))
