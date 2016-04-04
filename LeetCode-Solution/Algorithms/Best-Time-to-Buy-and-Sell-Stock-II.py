#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

    def maxProfit_another(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                result += (prices[i + 1] - prices[i])
        return result
