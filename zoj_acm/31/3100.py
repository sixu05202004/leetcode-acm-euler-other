#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cal(n):
    n.sort()
    n.remove(n[0])
    n.remove(n[-1])
    return sum(n) / len(n)


def zoj_3100():
    while True:
        line = int(raw_input())
        if line:
            t = []
            for i in range(line):
                a = int(raw_input())
                t.append(a)
            print cal(t)

        else:
            break

if __name__ == '__main__':
    zoj_3100()