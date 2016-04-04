#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        A = 0

        for n in nums:
            if n != val:
                nums[A] = n
                A += 1
        return A, nums
