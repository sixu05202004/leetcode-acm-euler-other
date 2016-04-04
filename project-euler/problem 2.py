#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import log


def fic(lim):
    n = log(lim * 5 ** .5) // log((2 + 5 ** .5))
    x = (2 + 5 ** .5)
    y = (2 - 5 ** .5)
    return int(((x - x ** (n + 1)) / (1 - x) - (y - y ** (n + 1)) / (1 - y)) / 5 ** .5)

print fic(4 * 10 ** 6)
