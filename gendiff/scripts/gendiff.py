#! /usr/bin/env python

import argparse
import json

parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', type=str, help='set format of output')

args = parser.parse_args()
print(args.first_file(args.second_file))


def generate_diff(filepath1, filepath2):
    file1 = json.load(filepath1)
    file2 = json.load(filepath2)
