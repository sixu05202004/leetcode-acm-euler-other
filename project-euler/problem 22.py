#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = []
f = open('D:\\Github\\project-euler\\names.txt', 'r')
for line in f:
    data.extend(line.split(","))
data = sorted([i.strip('"') for i in data])
result = []
for i in data:
    total = 0
    for j in i:
        total = total + (ord(j) - 64)
    result.append(total)
n = 0
for i in range(len(result)):
    n = n + ((i + 1) * result[i])
print n
