#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def zoj_2104():
    while True:
        num = int(raw_input())
        if num:
            data = {}
            for i in range(num):
                line = sys.stdin.readline()
                line = line.strip()

                if line in data.keys():
                    data[line] += 1
                else:
                    data[line] = 1
            a = sorted(data.keys(), key=data.__getitem__)
            print a[-1]
                #result.append(a[-1])
        else:
            break


if __name__ == '__main__':
    zoj_2104()
