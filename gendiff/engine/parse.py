""" Parsing command line arguments. """
import argparse
from gendiff.scripts.gendiff import generate_diff

DESCRIPTION = 'Difference generator'
FORMAT_FLAG_1 = '-f'
FORMAT_FLAG_2 = '--format'
FORMAT_HELP = "set format of output (default 'stylish')"
VERSION_STRING_1 = '-v'
VERSION_STRING_2 = '--version'
VERSION_NUMBER = '{0} 1.0'.format(DESCRIPTION)


def parsing_cli_arguments():
    """
    Функция по парсингу аргументов командой строки
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(VERSION_STRING_1, VERSION_STRING_2, action='version',
                        version='{0}'.format(VERSION_NUMBER))
    parser.add_argument(FORMAT_FLAG_1, FORMAT_FLAG_2,
                        help=FORMAT_HELP,
                        default='stylish')
    args = parser.parse_args()
    return args
