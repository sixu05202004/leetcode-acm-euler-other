#!/usr/bin/env python
# -*- coding: utf-8 -*-
out = """URL #%d
Protocol = %s
Host     = %s
Port     = %s
Path     = %s

"""


def zoj_1243():
    n = int(raw_input())
    for i in range(n):
        line = raw_input()
        line = line.split("://")
        Protocol = line[0]
        line = line[1]
        line = line.split("/", 1)
        if len(line) == 2:
            Path = line[1]
        else:
            Path = "<default>"
        line = line[0]
        line = line.split(":")
        if len(line) == 2:
            Port = line[1]
        else:
            Port = "<default>"
        Host = line[0]
        print "URL #%d" % (i + 1)
        print "Protocol = %s" % Protocol
        print "Host     = %s" % Host
        print "Port     = %s" % Port
        print "Path     = %s" % Path
        print ""


if __name__ == '__main__':
    zoj_1243()