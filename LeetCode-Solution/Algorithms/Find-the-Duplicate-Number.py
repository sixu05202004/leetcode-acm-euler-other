#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def findDuplicate_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        nums_dict = {}
        result = None
        for i in nums:
            if nums_dict.get(i):
                result = i
                break
            else:
                nums_dict[i] = 1
        return result

    def findDuplicate_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
