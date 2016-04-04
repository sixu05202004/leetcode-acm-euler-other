#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2176():
    while True:
        line = raw_input()
        num = int(line)
        if num == -1:
            break
        else:
            buff = list()
            for a in range(num):
                data = raw_input()
                data = data.split()
                data = [int(i) for i in data]
                buff.append(data)
            result = 0
            for i in range(len(buff)):
                if i == 0:
                    result += (buff[i][0] * buff[i][1])
                else:
                    result += (buff[i][0] * (buff[i][1] - buff[i - 1][1]))
            print "%d miles" % result

if __name__ == '__main__':
    zoj_2176()