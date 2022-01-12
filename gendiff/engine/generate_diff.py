from gendiff.engine.finding_difference import creating_difference
from gendiff.formats.formats import FORMATS, FORMAT_FILES
from gendiff.engine.parser_string import parsing_string_representation


def get_file_content(file_path):
    """
    Извлечение содержимого из файла.
    :param file_path: Путь до файла.
    :return: Расширение переданного файла
    """
    if file_path.endswith(FORMAT_FILES['json']):
        with open(file_path, 'r') as file:
            result = file.read()
        return parsing_string_representation(result)
    if file_path.endswith(FORMAT_FILES['yaml_yml']):
        with open(file_path, 'r') as file:
            result = file.read()
        return parsing_string_representation(result)


def generate_diff(file_path1, file_path2, style='stylish'):
    """ Главная функция по выводу конечных данных. """
    file1 = get_file_content(file_path1)
    file2 = get_file_content(file_path2)
    return FORMATS[style](creating_difference(file1, file2))
