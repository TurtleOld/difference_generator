from gendiff.engine.finding_difference import create_tree_vertices
from gendiff.formats.formats import FORMATS
from gendiff.engine.parse_content import parse_file_content


def generate_diff(file_path1, file_path2, output_format='stylish'):
    """ Главная функция по выводу конечных данных. """
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        result_content1 = file1.read()
        result_content2 = file2.read()

    return FORMATS[output_format](create_tree_vertices(
        parse_file_content(result_content1),
        parse_file_content(result_content2)
    ))
