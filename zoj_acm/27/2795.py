#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2795():
    while True:
        total = 0
        array = list()
        line = int(raw_input())
        if line:
            array.append(line)
            s = raw_input().split()
            s = [int(i) for i in s]
            array.extend(s)
            for i in range(1, len(array)):
                if array[array[i]] == i:
                    total += 1
                else:
                    break
            if total == len(s):
                print "ambiguous"
            else:
                print "not ambiguous"

        else:
            break

if __name__ == '__main__':
    zoj_2795()