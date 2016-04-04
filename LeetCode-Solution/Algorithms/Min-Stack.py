#!/usr/bin/env python
# -*- coding: utf-8


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float("+inf")

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if x < self.min:
            self.min = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack:
            r = self.stack.pop()
            if r == self.min and self.stack:
                self.min = min(self.stack)
            elif r == self.min and not self.stack:
                self.min = float("+inf")

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[len(self.stack) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.min
