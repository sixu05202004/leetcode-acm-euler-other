#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2481():
    out = []
    while True:
        data = raw_input()
        if len(data) > 1:
            t = data.split()
            t = t[1:]
            t = list(set(t))
            t.sort()
            out.append(t)
        else:
            break
    for i in out:
        print ' '.join(i)
if __name__ == '__main__':
    zoj_2481()
