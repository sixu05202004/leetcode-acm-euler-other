#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
data = []
total = 1

for line in sys.stdin:
    line = line.split("\n")[0]
    if line == '9':
        flag = 1
        for i in range(len(data) - 1):
            for j in range(i + 1, len(data)):
                if data[j] > data[i] and data[i] in data[j][:len(data[i])]:
                    flag = 0
                    break
        if flag:
            print "Set %d is immediately decodable" % total
        else:
            print "Set %d is not immediately decodable" % total
        total += 1
        data = []

    else:
        data.append(line)


while True:
    line = raw_input()
    if line == '9':
        flag = 1
        for i in range(len(data) - 1):
            for j in range(i + 1, len(data)):
                if data[j] > data[i] and data[i] in data[j][:len(data[i])]:
                    flag = 0
                    break
        if flag:
            print "Set %d is immediately decodable" % total
        else:
            print "Set %d is not immediately decodable" % total
        total += 1
        data = []

    else:
        data.append(line)
