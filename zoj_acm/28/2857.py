#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2857():
    count = 1
    while True:
        data = []
        out = []
        line = raw_input()
        if "0 0" in line:
            break
        else:
            line = [int(a) for a in line.split()]
            for i in range(3 * line[0]):
                s = raw_input().split()
                s = [int(a) for a in s]
                data.append(s)

            for z in range(line[0]):
                result = []
                for j in range(line[1]):
                    result.append(
                        str((data[z][j] + data[z + line[0]][j] + data[z + line[0] * 2][j]) / 3))
                out.append(result)

            print "Case %d:" % (count)
            for i1 in out:
                print ','.join(i1)
            count += 1


if __name__ == '__main__':
    zoj_2857()
