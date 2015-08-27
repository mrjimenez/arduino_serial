#!/usr/bin/python
# coding: utf-8

import fileinput
import sys

buffer_size = 0
threshold = 0
elapsed_time = 0.0

try:
    for line in fileinput.input(bufsize=0):
        l = line.split()
        if l:
            if l[0] == 'IMPORTANT:':
                if l[1] == 'Maximum':
                    pass
                elif l[1] == 'Buffer':
                    buffer_size = int(l[3][:-1])
                    threshold = int(l[5])
            elif l[0] == 'Elapsed':
                elapsed_time = float(l[2])
                print '{}, {}, {}'.format(buffer_size, threshold, elapsed_time)
                sys.stdout.flush()
except KeyboardInterrupt:
    pass

