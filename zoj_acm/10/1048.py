#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_1048():
    total = 0.00
    for i in range(12):
        input_data = raw_input()
        total = total + float(input_data)
    result = total / 12.00
    print '%s%.2f' % ('$', result)
if __name__ == '__main__':
    zoj_1048()