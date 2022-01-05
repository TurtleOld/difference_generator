import argparse
from gendiff import generate_diff, stylish

DESCRIPTION = 'Generate diff'
FORMAT_FLAG_1 = '-f'
FORMAT_FLAG_2 = '--format'
FORMAT_HELP = 'set format of output'


def parsing():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(FORMAT_FLAG_1, FORMAT_FLAG_2,
                        help=FORMAT_HELP,
                        default=stylish.get_stylish)
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))
