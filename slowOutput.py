#!/usr/bin/python
# coding: utf-8

import argparse
import sys
import time

my_parser = argparse.ArgumentParser(
    description='Slowly output the lines of a text file.',
    epilog='Parameters can be in a file, one per line, using @"file name"',
    fromfile_prefix_chars='@')
my_parser.add_argument(
    'fileNames',
    nargs='+',
    type=argparse.FileType(mode='r'),
    default=sys.stdin,
    help='File to parse.'
         ' (type %(type)s)')
args = my_parser.parse_args()


def main():
    for fd in args.fileNames:
        with fd:
            try:
                for line in fd:
                    print line,
                    sys.stdout.flush()
                    time.sleep(0.5)
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    main()
