#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2781():
    n = int(raw_input())
    for i in range(n):
        line = raw_input()
        if len(line) == 1:
            print line
        else:
            t = [int(i) for i in line[::-1]]
            for i in range(len(t) - 1):
                if t[i] < 5:
                    t[i] = 0
                else:
                    t[i] = 0
                    t[i + 1] = t[i + 1] + 1
            t.reverse()
            t = [str(i) for i in t]
            print ''.join(t)

if __name__ == '__main__':
    zoj_2781()