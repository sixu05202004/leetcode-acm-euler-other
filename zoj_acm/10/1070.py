#!/usr/bin/env python
# -*- coding: utf-8 -*-


from math import sqrt


def bodeplot(vs, r, c, w):
    return round(vs * r * c * w / (sqrt(vs ** 2 * c ** 2 * w ** 2 + 1)), 3)

line = raw_input()
vs, r, c, num = line.split()
result = []
for i in range(int(num)):
    line = raw_input()
    w = line.split()
    result.append(bodeplot(float(vs[0]), float(r[0]), float(c[0]), float(w[0])))
for i in result:
    print '%.3f' % i
