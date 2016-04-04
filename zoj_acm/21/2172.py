#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = 1
while True:
    line = int(raw_input())
    if line:
        data = list()
        for i in range(line):
            s = raw_input()
            data.append(s)
        sorted(data, key=lambda i: len(i))
        print "SET %d" % num
        for i in range(0, len(data), 2):
            print data[i]
        if len(data) % 2:
            for i in range(len(data) - 2, -1, -2):
                print data[i]
        else:
            for i in range(len(data) - 1, -1, -2):
                print data[i]
        num += 1

    else:
        break
