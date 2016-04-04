#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
20 = 2^2 * 5
19 = 19
18 = 2 * 3^2
17 = 17
16 = 2^4
15 = 3 * 5
14 = 2 * 7
13 = 13
11 = 11

2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232 792 560
'''


def pep5():
    f_value = [8, 9, 12, 16, 18, 20]
    i = 1
    while 1:
        i += 1
        count = 0
        for v in f_value:

            if (9699690 * i) % v:
                continue
            else:
                count += 1
            if count == 6:
                return 9699690 * i


if __name__ == '__main__':
    print pep5()
