#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
i = [i for i in xrange(1, 1000001) if i % 3 == 0 or i % 5 == 0]
for line in sys.stdin:
    line = line.split()
    print i[int(line[0]) - 1]
