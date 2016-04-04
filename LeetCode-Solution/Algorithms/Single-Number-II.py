#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for i in nums:
            result[i] = result.get(i, 0) + 1
        for (k, v) in result.items():
            if v == 1:
                return k

    def singleNumber_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(3):
            for num in nums:
                res ^= num
        return res
