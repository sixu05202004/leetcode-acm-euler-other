#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
(1+2+...+n)^2 =((1+n)^2 * n^2)/4

1^2 + 2^2 + ... + n^2 = n*(n+1)*(2n+1)/6
'''


def pep6(n):
	return (3*(n**4)+2*(n**3)-3*(n**2)-2*n)/12

if __name__ == '__main__':
	print pep6(100)