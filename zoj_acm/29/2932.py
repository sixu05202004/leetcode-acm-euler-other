#!/usr/bin/env python
# -*- coding: utf-8 -*-

table = {
    " ": "%20",
         "!": "%21",
         "$": "%24",
         "(": "%28",
         ")": "%29",
         "*": "%2a"
}


def zoj_2932():
    while True:
        line = raw_input()
        if line == "#":
            break
        else:
            if "%" in line:
                line = line.replace("%", "%25")
            for i in line:
                if i in table.keys():
                    line = line.replace(i, table.get(i))
            print line

if __name__ == '__main__':
    zoj_2932()