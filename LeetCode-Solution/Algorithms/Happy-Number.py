#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n >= 10:
            s = 0
            str_n = str(n)
            for num in str_n:
                num = int(num)
                nn = num * num
                s += nn
            n = s
        return n == 1 or n == 7
