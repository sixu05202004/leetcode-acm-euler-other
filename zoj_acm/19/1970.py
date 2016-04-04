#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def zoj_1970():
    for line in sys.stdin:
        line = line.split()
        count = 0
        for i in line[1]:
            if line[0][count] == i:
                count += 1
                if count >= len(line[0]):
                    break
        if count >= len(line[0]):
            print 'Yes'
        else:
            print 'No'


if __name__ == '__main__':
    zoj_1970()
