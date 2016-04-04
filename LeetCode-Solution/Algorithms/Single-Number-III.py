#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        output = []
        for i in nums:
            result[i] = result.get(i, 0) + 1
        for (k, v) in result.items():
            if v == 1:
                output.append(k)
        return output

    def singleNumber_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res1, res2 = 0, 0
        for num in nums:
            res1 ^= num
        for num in nums[::-1]:
            res2 ^= num
        return [res1, res2]
