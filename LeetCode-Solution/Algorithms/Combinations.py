#!/usr/bin/env python
# -*- coding: utf-8

import itertools


class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        return list(itertools.combinations((i for i in range(1, n + 1)), k))
