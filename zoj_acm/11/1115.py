#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cal(s):
    while True:
        t = [int(i) for i in s]
        if sum(t) < 10:
            return sum(t)
        else:
            s = str(sum(t))


def zoj_1115():
    result = []
    while True:
        data = raw_input()
        if int(data):
            r = cal(data)
            result.append(r)
        else:
            break
    for i in result:
        print i

if __name__ == '__main__':
    zoj_1115()
