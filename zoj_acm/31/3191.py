#!/usr/bin/env python
# -*- coding: utf-8 -*-
table = {
    "Exactly 3 o'clock": [0, 360],
    "Between 2 o'clock and 3 o'clock": range(1, 30),
    "Exactly 2 o'clock": [30],
    "Between 1 o'clock and 2 o'clock": range(31, 60),
    "Exactly 1 o'clock": [60],
    "Between 0 o'clock and 1 o'clock": range(61, 90),
    "Exactly 0 o'clock": [90],
    "Between 11 o'clock and 0 o'clock": range(91, 120),
    "Exactly 11 o'clock": [120],
    "Between 10 o'clock and 11 o'clock": range(121, 150),
    "Exactly 10 o'clock": [150],
    "Between 9 o'clock and 10 o'clock": range(151, 180),
    "Exactly 9 o'clock": [180],
    "Between 8 o'clock and 9 o'clock": range(181, 210),
    "Exactly 8 o'clock": [210],
    "Between 7 o'clock and 8 o'clock": range(211, 240),
    "Exactly 7 o'clock": [240],
    "Between 6 o'clock and 7 o'clock": range(241, 270),
    "Exactly 6 o'clock": [270],
    "Between 5 o'clock and 6 o'clock": range(271, 300),
    "Exactly 5 o'clock": [300],
    "Between 4 o'clock and 5 o'clock": range(301, 330),
    "Exactly 4 o'clock": [330],
    "Between 3 o'clock and 4 o'clock": range(331, 360)
}


def zoj_3191():
    while True:
        line = int(raw_input())
        if line == -1:
            break
        else:
            for i in table.iteritems():
                if line in i[1]:
                    print i[0]


if __name__ == '__main__':
    zoj_3191()