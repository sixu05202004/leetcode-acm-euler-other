#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
l = 0
hr = 1
for line in sys.stdin:
    str = line.split()

    for item in str:
        if item == '<hr>':
            if hr == 0:
                print '\n' + '-' * 80
                hr = 1
                l = 0
            else:
                print '-' * 80
                l = 0
        else:
            if l + len(item) > 80:
                sys.stdout.write('\n' + item)
                l = len(item) + 1
                hr = 0
            elif item == '<br>':
                hr = 1
                print ''
                l = 0
            else:
                if(hr == 1):
                    sys.stdout.write(item)
                else:
                    sys.stdout.write(' ' + item)
                l += len(item) + 1
                hr = 0
