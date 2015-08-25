#!/usr/bin/python
# coding: utf-8

import argparse
import sys
import Uploader

my_parser = argparse.ArgumentParser(
    description='XSVF file processor.',
    epilog='Parameters can be in a file, one per line, using @"file name"',
    fromfile_prefix_chars='@')
my_parser.add_argument(
    '-v', '--version',
    action='version',
    version='%(prog)s version 1.0.0')
my_parser.add_argument(
    '-d', '--debug',
    default=1,
    type=int,
    help='Debug verbosity'
         ' (type %(type)s, default=%(default)s)')
my_parser.add_argument(
    '-i', '--iterations',
    default=3,
    type=int,
    help='Debug verbosity'
         ' (type %(type)s, default=%(default)s)')


def main():
    Uploader.Uploader.add_arguments(my_parser)
    args = my_parser.parse_args()
    u = Uploader.Uploader(args)
    fileNameList = []
    for i in range(0, args.iterations):
        fileNameList.append(open("/dev/zero", mode='r'))
    u.upload_all_files(fileNameList)
    error_code = u.error_code
    sys.exit(error_code)

if __name__ == '__main__':
    main()
