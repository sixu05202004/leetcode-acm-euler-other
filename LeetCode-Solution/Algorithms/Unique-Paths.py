#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        T(m,n) = T(m-1, n) + T(m, n-1)
        """
        if not m or not n:
            return 0
        T = [[0] * n] * m
        for i in range(m):
            T[i][0] = 1
        for i in range(n):
            T[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                T[i][j] = T[i - 1][j] + T[i][j - 1]
        return T[m - 1][n - 1]
