#!/usr/bin/env python
# -*- coding: utf-8 -*-



def pep9():
    for a in range(1, 334):
        for c in range(int((2 ** .5) * a) + 1, 499):
            if a * a + (1000 - a - c) ** 2 == c ** 2:
                return a * (1000 - a - c) * c

if __name__ == '__main__':
    print pep9()