#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pep4():
    result = []
    for x in xrange(999, 99, -1):
        for y in xrange(999, 99, -1):
            if str(x * y) == str(x * y)[::-1]:
                result.append(x * y)
    return max(result)
if __name__ == '__main__':
    print pep4()
