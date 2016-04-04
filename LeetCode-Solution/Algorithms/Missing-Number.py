#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def missingNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        nums_len = len(nums)
        result = set(range(nums_len + 1)) - set(nums)
        return result.pop()

    def missingNumber_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        nums_len = len(nums)
        total = (nums_len + 1) * nums_len / 2
        return total - reduce(lambda x, y: x + y, nums)

    def missingNumber_3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        nums_len = len(nums)
        total = (nums_len + 1) * nums_len / 2
        for i in nums:
            total -= i
        return total
