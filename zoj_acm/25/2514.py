#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
table = {'1': '@',
         '0': '%',
         'l': 'L',
         'O': 'o'}


def zoj_2514():

    while True:
        num = int(raw_input())
        result = []
        a = 0
        if num:
            for i in range(num):
                total = 0
                line = sys.stdin.readline()
                line = line.strip().split()
                for i in ['1', '0', 'l', 'O']:
                    if i in line[1]:
                        total += 1
                        a += 1
                        line[1] = line[1].replace(i, table.get(i))
                if total:
                    result.append(line)
            if a == 0:
                print "No account is modified."
            else:
                print len(result)
                for i in result:
                    print " ".join(i)
        else:
            break


if __name__ == '__main__':
    zoj_2514()