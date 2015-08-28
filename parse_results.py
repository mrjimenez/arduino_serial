#!/usr/bin/python
# coding: utf-8

import argparse
import sys

my_parser = argparse.ArgumentParser(
    description='Text result parser.',
    epilog='Parameters can be in a file, one per line, using @"file name"',
    fromfile_prefix_chars='@')
my_parser.add_argument(
    'fileName',
    nargs='?',
    type=argparse.FileType(mode='r'),
    default=sys.stdin,
    help='File to parse.'
         ' (type %(type)s)')
args = my_parser.parse_args()


buffer_size = 0
threshold = 0
elapsed_time = 0.0


def process_line(line):
    global buffer_size
    global threshold
    global elapsed_time
    l = line.split()
    if l:
        if l[0] == 'IMPORTANT:':
            if l[1] == 'Buffer':
                buffer_size = int(l[3][:-1])
                threshold = int(l[5])
            # elif l[1] == 'Maximum':
            #    pass
        elif l[0] == 'Elapsed':
            elapsed_time = float(l[2])
            print '{}, {}, {}'.format(buffer_size, threshold, elapsed_time)
            sys.stdout.flush()


def main():
    while True:
        try:
            line = args.fileName.readline()
        except KeyboardInterrupt:
            break
        if not line:
            break
        process_line(line)
        # sys.stdout.write(line)
        # print line,

if __name__ == '__main__':
    main()
