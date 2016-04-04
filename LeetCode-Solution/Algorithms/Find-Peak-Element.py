#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return
        elif nums and len(nums) == 1:
            return 0
        result = None
        for i in range(len(nums)):
            if i == 0:
                right = nums[i + 1]
                left = float("-inf")
            elif i == len(nums) - 1:
                left = nums[i - 1]
                right = float("-inf")
            else:
                left = nums[i - 1]
                right = nums[i + 1]
            if nums[i] > left and nums[i] > right:
                result = i
                break
        return result
