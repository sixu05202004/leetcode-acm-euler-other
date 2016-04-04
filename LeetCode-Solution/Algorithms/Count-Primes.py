#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return 0
        else:
            return self.primer(n)

    def primer(self, n):
        import math
        L = [True] * n

        def seive(x):
            for i in xrange(x * 2, n, x):
                L[i] = False
        map(seive, [2])
        map(seive, xrange(3, int(math.ceil(math.sqrt(n))), 2))
        return L.count(True) - 2
