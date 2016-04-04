#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2480():
    while True:
        n = int(raw_input())
        if n:
            result = []
            for i in range(n):
                line = raw_input()
                x1, y1, x2, y2 = line.split()
                result.append([(int(x1), int(x2)), (int(y1), int(y2))])
            s = int(raw_input())
            for i in range(s):
                t = -1
                line = raw_input().split()
                line = [int(i) for i in line]
                for i in range(len(result) - 1, -1, -1):
                    if line[0] in range(result[i][0][0], result[i][0][1] + 1) and line[1] in range(result[i][1][0], result[i][1][1] + 1):
                        t = i
                        break
                print t

        else:
            break

if __name__ == '__main__':
    zoj_2480()