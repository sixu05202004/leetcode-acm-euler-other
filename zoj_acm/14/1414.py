#!/usr/bin/env python
# -*- coding: utf-8 -*-


def even(n):
    if n:
        return even(n - 1) + 1 + ((n - 1) % 2) * 2
    else:
        return 0


def odd(n):
    return even(n - 2) + 2


def zoj_1414():
    num = int(raw_input())
    for i in range(num):
        line = raw_input()
        line = [int(i) for i in line.split()]
        if line[0] == line[1]:
            print even(line[0])
        elif line[0] - line[1] == 2 and line[0] >= 2:
            print odd(line[0])
        else:
            print "No Number"

if __name__ == '__main__':
    zoj_1414()
