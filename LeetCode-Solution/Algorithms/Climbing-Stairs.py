#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        first = 1
        sencond = 2
        i = 3
        while i < n:
            asencond = first + sencond
            first, sencond = sencond, asencond
            i += 1
        return first + sencond
