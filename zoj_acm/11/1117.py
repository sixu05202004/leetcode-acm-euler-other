#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Queue import PriorityQueue
from copy import copy


class Node(object):

    def __init__(self, weight=0, right=None, left=None):
        self.weight = weight
        self.right = right
        self.left = left


class Leaf(object):

    def __init__(self, key='', weight=0):
        self.key = key
        self.weight = weight


class Huffman(object):

    """
    item must be [('a',3),('b',4),('c',5)]
    """

    def __init__(self, item):
        self.root = None
        self.item = item
        self.dict = dict()
        self.queue = PriorityQueue()
        self.build()
        self.encode()

    def __proc_leaf(self):
        for key, weight in self.item:
            leaf = Leaf(key, weight)
            self.queue.put((weight, leaf))

    def build(self):
        self.__proc_leaf()
        for i in range(len(self.item) - 1):
            left = self.queue.get()[1]
            right = self.queue.get()[1]
            weight = left.weight + right.weight
            node = Node(weight, left, right)
            self.queue.put((weight, node))
        self.root = self.queue.get()[1]

    def encode(self):

        def genEncodeHelp(root, array=[]):
            if isinstance(root, Leaf):
                self.dict[root.key] = copy(array)
                return
            array.append(0)
            genEncodeHelp(root.left, array)
            array[len(array) - 1] = 1
            genEncodeHelp(root.right, array)
            array.pop()
        genEncodeHelp(self.root)


def zoj_1117():
    while True:
        line = raw_input()
        if line == "END":
            break
        else:
            bitlen = 0
            lenght = len(line)
            total = dict()
            in_put = list()
            set_t = set(line)
            if len(set_t) == 1:
                print "%d %d %.1f" % (lenght * 8, lenght, 8.0)
            else:
                for item in set_t:
                    num = line.count(item)
                    total[item] = num
                    in_put.append((item, num))
                in_put = sorted(in_put, key=lambda i: i[1])
                result = Huffman(in_put)
                for item in set_t:
                    bitlen = bitlen + len(result.dict[item]) * total[item]
                rario = lenght * 8.0 / bitlen
                print "%d %d %.1f" % (lenght * 8, bitlen, rario)


if __name__ == '__main__':
    zoj_1117()
