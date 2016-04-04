#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        pos = 1
        now = nums[0]
        for cursor in xrange(1, len(nums)):
            if nums[cursor] == now:
                continue
            nums[pos], nums[cursor] = nums[cursor], nums[pos]
            now = nums[pos]
            pos += 1

        return pos
