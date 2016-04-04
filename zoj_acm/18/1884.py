#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import string

for line in sys.stdin:
    line = line.rstrip("\n")
    b = "`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
    a = "1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./`"
    table = string.maketrans(a, b)
    print string.translate(line, table)
