#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
