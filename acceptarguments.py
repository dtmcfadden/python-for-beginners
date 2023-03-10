# Accepting Arguments

import sys

# name = sys.argv[1]

# print(sys.argv)
# print(f'Hello {name}')

import argparse

parser = argparse.ArgumentParser(
    description='This program prints the name of my dogs'
)

parser.add_argument('-c', '--color', metavar='color',
                    choices={'red', 'yellow'},
                    required=True, help='the color to search for')

args = parser.parse_args()

print(args.color)
