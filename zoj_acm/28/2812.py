#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2812():
    while True:
        line = raw_input()
        total = 0
        if line == "#":
            break
        else:
            for i in range(len(line)):
                if line[i] != " ":
                    total = total + (ord(line[i]) - 64) * (i + 1)
            print total


if __name__ == '__main__':
    zoj_2812()