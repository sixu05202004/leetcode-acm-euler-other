#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        maxnums = nums[0]
        for i in nums:
            if i < maxnums:
                maxnums = i
        return maxnums
