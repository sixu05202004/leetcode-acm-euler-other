#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2987():
    n = int(raw_input())
    for j in range(n):
        line = raw_input().split()
        s = int(line[0])
        array_str = [i for i in line[1]]
        array_str = [array_str[i] for i in range(len(array_str)) if i != s - 1]
        out = ''.join(array_str)
        print "%d %s" % (j + 1, out)


if __name__ == '__main__':
    zoj_2987()