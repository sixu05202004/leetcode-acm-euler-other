#!/usr/bin/env python
# -*- coding: utf-8 -*-


while True:
    line = raw_input()
    if "0 0 0 0 0 0" in line:
        break
    else:
        line = [int(i) for i in line.split()]
        a1 = line[2] + line[4]
        a2 = line[3] + line[5]
        print "Anna's won-loss record is %d-%d." % (a2 - line[0], a1 - line[1])
