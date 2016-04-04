#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2722():
    while True:
    	line = int(raw_input())
    	count = 0
    	if line:
        	while line > 1:
        		t = line % 2
        		line = line / 2
        		line += t
        		count += 1
        	print count
    	else:
        	break


if __name__ == '__main__':
    zoj_2722()
