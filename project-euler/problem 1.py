#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
3,6,9,12,...: 3(1,2,3,...)
5,10,15,20,...: 5(1,2,3,...)
15,30,45,...: 15(1,2,3,...)
'''


def cal(base, num):
    num = num / base
    return base * (num + 1) * num / 2


def main():
    print cal(3, 999) + cal(5, 999) - cal(15, 999)

if __name__ == '__main__':
    main()
