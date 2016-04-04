#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2417():
    while True:
        n = int(raw_input())
        if n:
            line = bin(n)
            for i in range(len(line) - 1, 1, -1):
                if line[i] == "1":
                    result = line[i:]
                    print int(result, 2)
                    break

        else:
            break

if __name__ == '__main__':
    zoj_2417()
