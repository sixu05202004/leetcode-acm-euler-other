#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_3174():
    n = int(raw_input())
    for i in range(n):
        line = raw_input().split()
        line = [int(line[0]), int(line[1])]
        count = 0
        for year in range(line[0], line[1] + 1):
            for j in range(1, 13):
                if (j ** 2 == year % 100) or (j ** 2 == year % 1000):
                    count += 1
                    break
        print count


if __name__ == '__main__':
    zoj_3174()