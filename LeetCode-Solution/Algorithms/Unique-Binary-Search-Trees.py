#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        卡特兰数
        """
        if n == 1:
            return 1
        last_value = 1
        for i in range(1, n + 1):
            t = last_value * (4 * i - 2) / (i + 1)
            last_value = t
        return last_value
