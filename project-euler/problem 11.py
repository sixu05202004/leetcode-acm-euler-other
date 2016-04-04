#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = list()
f = open('problem11.txt', 'r')
for line in f.readlines():
    line = line.split()
    last = [int(a) for a in line]
    data.append(last)


def pe11():
    maxnum = 0
    for i in range(20):
        for j in range(20):
            right = data[i][j] * data[i + 1][j] * data[i + 2][j] * data[i + 3][j]
            down = data[i][j] * data[i][j + 1] * data[i][j + 2] * data[i][j + 3]
            diag = data[i][j] * data[i + 1][j + 1] * data[i + 2][j + 2] * data[i + 3][j + 3]
            diag1 = 0
            if j >= 3:
                diag1 = data[i][j] * data[i + 1][j - 1] * data[i + 2][j - 2] * data[i + 3][j - 3]

            if max(right, down, diag, diag1) > maxnum:
                maxnum = max(right, down, diag, diag1)
    return maxnum
if __name__ == '__main__':
    print pe11()
