#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2478():
    n = int(raw_input())
    for i in range(n):
        line = raw_input()
        if len(line) == 1:
            print line
        else:
            j = 1
            line = line + '0'
            c = line[0]
            total = 1
            result = ''
            while j < len(line):

                if line[j] == c:
                    total += 1
                else:
                    if total != 1:
                        result = result + str(total) + c
                    else:
                        result = result + c
                    total = 1
                    c = line[j]
                j += 1
            print result


if __name__ == '__main__':
    zoj_2478()
