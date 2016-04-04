#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2201():
    line = raw_input()
    num = int(line)
    result = []
    for a in range(num):
        data = raw_input()
        data = data.split()
        if int(data[0]) >= int(data[1]):
            result.append("MMM BRAINS")
        else:
            result.append("NO BRAINS")
    for i in result:
        print i


if __name__ == '__main__':
    zoj_2201()