#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ip_string(n):
    result = []
    for i in range(4):
        result.append(str(n % 256))
        n = n / 256
    result.reverse()
    return '.'.join(result)

out = []


def zoj_2482():
    n = int(raw_input())
    for i in range(n):
        data = int(raw_input(), 2)
        out.append(ip_string(data))
    for i in out:
        print i

if __name__ == '__main__':
	zoj_2482()
