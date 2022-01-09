from gendiff.engine.finding_difference import determining_file_format,\
    creating_difference
from gendiff.formats.styles import FORMATS


def generate_diff(file_path1, file_path2, style='stylish'):
    """ Главная функция по выводу конечных данных. """
    file1 = determining_file_format(file_path1)
    file2 = determining_file_format(file_path2)
    return FORMATS[style](creating_difference(file1, file2))
