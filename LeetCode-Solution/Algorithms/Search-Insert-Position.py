#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        lastindex = -1
        for i in range(len(nums)):
            if nums[i] == target:
                lastindex = i - 1
                break
            elif target > nums[i]:
                lastindex = i
            elif target < nums[i]:
                break
        return lastindex + 1
