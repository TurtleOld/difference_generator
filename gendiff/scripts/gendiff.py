""" Launch program Generator Difference """
# ! /usr/bin/env python

from gendiff.engine.parse import parsing_cli_arguments
from gendiff.engine.generate_diff import generate_diff


def main():
    """ Главная функция по запуску пакета. """
    args = parsing_cli_arguments()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
