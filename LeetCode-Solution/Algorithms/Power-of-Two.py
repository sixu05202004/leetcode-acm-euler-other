#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if not n & (n - 1):
            return True
        else:
            return False
