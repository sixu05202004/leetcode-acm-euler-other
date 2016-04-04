#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pro(n):
    result = []
    while True:
        if len(n) > 3:
            result.append(n[len(n) - 3:])
            n = n[:len(n) - 3]
        else:
            result.append(n)
            break
    result.reverse()
    return ','.join(result)


def zoj_2476():
    result = []
    while True:
        buff = []
        num = int(raw_input())
        if num:
            for i in range(num):
            	buff.append(float(''.join(raw_input().lstrip('$').split(','))))
            temp = "%.2f" % sum(buff)
            temp = temp.split('.')
            temp[0] = pro(temp[0])
            result.append("$" + '.'.join(temp))

        else:
            break

    for i in result:
        print i

if __name__ == '__main__':
    zoj_2476()
