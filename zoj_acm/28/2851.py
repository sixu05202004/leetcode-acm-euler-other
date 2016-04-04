#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2851():
    n = int(raw_input())
    for i in range(n):
        tabtotal = 0
        spacetotal = 0
        while True:
            line = raw_input()
            if line == "##":
                break
            else:
                tabtotal = tabtotal + line.count("\t")
                for i in range(len(line) - 1, -1, -1):
                    if line[i] == " ":
                        spacetotal += 1
                    elif line[i] == "\t":
                        spacetotal += 4
                    else:
                        break
        print "%d tab(s) replaced" % tabtotal
        print "%d trailing space(s) removed" % spacetotal

if __name__ == '__main__':
    zoj_2851()
