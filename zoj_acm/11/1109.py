#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

table = {}
for line in sys.stdin:
    line = line.split()
    if len(line) >= 2:
        table[line[1]] = line[0]
    elif len(line) == 1:
        if table.get(line[0]):
            print table[line[0]]
        else:
            print "eh"

    else:
        continue
