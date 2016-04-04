#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
for line in sys.stdin:
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    print a - 3 * b + 3 * c, 3 * a - 8 * b + 6 * c, 6 * a - 15 * b + 10 * c
