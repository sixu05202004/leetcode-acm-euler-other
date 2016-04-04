#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2947():
    n = int(raw_input())
    for i in range(n):
        t1 = int(raw_input())
        line1 = raw_input().split()
        t2 = int(raw_input())
        line2 = raw_input().split()
        if t1 == t2:
            line1 = [j[0] for j in line1]
            line2 = [j[0] for j in line2]
            if ''.join(line1) == ''.join(line2):
                print "SAME"
            else:
                print "DIFFERENT"
        else:
            print "DIFFERENT"

if __name__ == '__main__':
    zoj_2947()
