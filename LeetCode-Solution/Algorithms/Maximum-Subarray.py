#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        maxnum = float("-inf")
        tempsum = 0
        for i in nums:
            tempsum += i
            if tempsum > maxnum:
                maxnum = tempsum
            if tempsum <= 0:
                tempsum = 0
        return maxnum
