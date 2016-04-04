#!/usr/bin/env python
# -*- coding: utf-8 -*-


def floyd_b(result, n):
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if result[i][k] * result[k][j] > result[i][j]:
                    result[i][j] = result[i][k] * result[k][j]
    return result


def zoj_1092():
    total = 1
    while True:
        line = int(raw_input())
        data = list()
        if line:
            # init data
            result = [[0 for i in range(line)] for j in range(line)]
            for i in range(line):
                result[i][i] = 1.00
            for i in range(line):
                s = raw_input()
                data.append(s)
            t = int(raw_input())
            for i in range(t):
                line = raw_input().split()
                a = data.index(line[0])
                b = data.index(line[2])
                element = float(line[1])
                result[a][b] = element
            floyd_b(result, len(result))
            flag = 0
            for i in range(len(result)):
                if result[i][i] > 1.00:
                    flag = 1
                    break
            if flag:
                print "Case %d: Yes" % total
            else:
                print "Case %d: No" % total
            total += 1
            line = raw_input()

        else:
            break

if __name__ == '__main__':
    zoj_1092()