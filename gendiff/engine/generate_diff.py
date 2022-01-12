from gendiff.engine.finding_difference import creating_difference
from gendiff.formats.formats import FORMATS
from gendiff.engine.parser_string import parsing_string_representation


def generate_diff(file_path1, file_path2, output_format='stylish'):
    """ Главная функция по выводу конечных данных. """
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        result_content1 = file1.read()
        result_content2 = file2.read()

    return FORMATS[output_format](creating_difference(
        parsing_string_representation(result_content1),
        parsing_string_representation(result_content2)
    ))
