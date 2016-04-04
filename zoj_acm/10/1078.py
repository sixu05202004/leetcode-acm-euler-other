#!/usr/bin/env python
# -*- coding: utf-8 -*-
table = {
    10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f',
        16: 'g'
}


def base_n(n, base):
    t = []
    while n > 0:
        a = n % base
        if a >= 10:
            t.append(table.get(a))
        else:
            t.append(str(a))
        n = n / base

    t1 = ''.join(t)
    t.reverse()
    t2 = ''.join(t)
    return t1 == t2


def zoj_1078():
    while True:
        result = []
        n = int(raw_input())
        if not n:
            break
        else:
            for i in range(2, 17):
                if base_n(n, i):
                    result.append(i)
            if result:
                result = [str(i) for i in result]
                out = " ".join(result)
                print "Number %d is palindrom in basis %s" % (n, out)
            else:
                print "Number %d is not a palindrom" % n

if __name__ == '__main__':
    zoj_1078()
