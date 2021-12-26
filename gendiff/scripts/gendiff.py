#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', type=str, help='set format of output')

args = parser.parse_args()
print(args.first_file(args.second_file))
