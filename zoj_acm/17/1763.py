#!/usr/bin/env python
# -*- coding: utf-8 -*-

i = 0
result = 0.00
while True:
    line = raw_input()
    if line == "999":
        print "End of Output"
        break
    else:
        if i:
            print "%.2f" % (float(line) - result)
        result = float(line)
    i += 1
