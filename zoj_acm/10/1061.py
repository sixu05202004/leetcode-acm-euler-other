#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_1061():
    n = int(raw_input())
    for i in range(n):
        result = {0: "http://www.acm.org/"}
        flag = 0
        lenght = 0
        while True:
            line = raw_input()
            if line and 'QUIT' not in line:
                line = line.split()
                if len(line) == 2:
                    if lenght - flag >= 2:
                        for j in range(flag + 2, lenght + 3):
                            result.pop(j)
                    flag = flag + 1
                    lenght = flag

                    result[lenght] = line[1]
                    print line[1]
                else:
                    if line[0] == "BACK" and result.get(flag - 1):
                        print result.get(flag - 1)
                        flag = flag - 1
                    elif line[0] == "FORWARD" and result.get(flag + 1):
                        print result.get(flag + 1)
                        flag = flag + 1
                    else:
                        print "Ignored"
            elif 'QUIT' in line:
                break
            else:
                continue


if __name__ == '__main__':
    zoj_1061()
