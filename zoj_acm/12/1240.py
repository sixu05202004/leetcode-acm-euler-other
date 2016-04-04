#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
orgin = "abcdefghijklmnopqrstuvwxyz".upper()
changeto = "bcdefghijklmnopqrstuvwxyza".upper()
table = string.maketrans(orgin, changeto)
n = int(raw_input())
for i in range(n):
    line = raw_input()
    print "String #%d\n%s\n" % (i + 1, string.translate(line, table))
