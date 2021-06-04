import os
import sys


def main():
    dir_name = sys.argv[1]

    os.mkdir(dir_name)

    with open('template.py', 'r') as f:
        c = f.read()

    for file_name in ['a', 'b', 'c', 'd', 'e', 'f']:
        with open(f'{dir_name}/{file_name}.py', 'a') as f:
            f.write(c)
