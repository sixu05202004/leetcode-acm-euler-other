#!/usr/bin/env python
# -*- coding: utf-8 -*-
data = [[4.5, 150, 200], [6.0, 300, 500], [5.0, 200, 300]]
name = {
    0: "Wide Receiver",
    1: "Lineman",
    2: "Quarterback"
}


def zoj_2321():
    result = []
    while True:
        line = raw_input()
        if "0 0 0" in line:
            break
        else:
            line = line.split()
            line = [float(line[0]), int(line[1]), int(line[2])]
            t = []
            for i in range(3):
                if line[0] <= data[i][0] and line[1] >= data[i][1] and line[2] >= data[i][2]:
                    t.append(name.get(i))
                    continue
            if t:
                result.append(t)
            else:
                result.append(["No positions"])
    for i in result:
        if len(i) == 1:
            print "".join(i)
        else:
            print " ".join(i)

if __name__ == '__main__':
    zoj_2321()
