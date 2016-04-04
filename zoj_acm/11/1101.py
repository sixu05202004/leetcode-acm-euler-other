#!/usr/bin/env python
# -*- coding: utf-8 -*-




while True:
    line = int(raw_input())
    if line:
        flag = False
        result = 0
        array = list()
        for i in range(line):
            n = int(raw_input())
            array.append(n)
        array.sort()
        for i in range(line - 1, 2, -1):
            for j in range(i-1, 1, -1):
                for z in range(j-1, 0, -1):
                    for k in range(z-1, -1, -1):
                        else:
                            if array[j] + array[z] + array[k] == array[i]:
                                flag = True
                                result = array[i]
                    if flag:
                        break
                if flag:
                    break
            if flag:
                break

        if flag:
            print result
        else:
            print "no solution"

    else:
        break
