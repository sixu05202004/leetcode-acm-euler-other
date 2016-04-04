#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pe3(num, value):
    i = 2
    while i < num:
        if not value % i:
            value = value / i
            if value == 1:
                return i
            continue

        i += 1

if __name__ == '__main__':
    print pe3(775147, 600851475143)
