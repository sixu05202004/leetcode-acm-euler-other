#!/usr/bin/env python
# -*- coding: utf-8 -*-
import decimal
data = list()
f = open('problem13.txt', 'r')
for line in f.readlines():
    line = decimal.Decimal(line.strip())
    data.append(line)

print sum(data)
