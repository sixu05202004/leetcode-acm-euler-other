#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

table = [1, 2, 0, 2, 2, 1, 0, 1]
for line in sys.stdin:
    line = int(line)
    if table[line % 8] == 0:
        print "yes"
    else:
        print "no"
