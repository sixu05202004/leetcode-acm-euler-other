#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = [362880, 40320, 5040, 720, 120, 24, 6, 2, 1]


def zoj_2358():
    result = []
    while True:
        num = int(raw_input())
        if num < 0:
            break
        elif num == 0:
            result.append("NO")
        else:
            for i in f:
                if num >= i:
                    num = num - i
            if num == 0:
                result.append("YES")
            else:
                result.append("NO")
    if result:
        for i in result:
            print i

if __name__ == '__main__':
    zoj_2358()