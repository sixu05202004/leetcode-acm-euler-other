#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2886():
    n = int(raw_input())
    for i in range(n):
        line = raw_input()

        j = 1
        line = line + 'a'
        c = line[0]
        total = 1
        result = ''
        while j < len(line):

            if line[j] == c:
                total += 1
            else:

                result = result + str(total) + c

                total = 1
                c = line[j]
            j += 1
        print result


if __name__ == '__main__':
    zoj_2886()
