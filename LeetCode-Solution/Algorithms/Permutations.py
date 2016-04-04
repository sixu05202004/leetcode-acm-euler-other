#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = [nums]
        nums_len = len(nums)

        for i in xrange(1, nums_len):
            result_len = len(result)
            for k in xrange(result_len):
                for j in xrange(i):
                    result.append(result[k][:])
                    result[-1][j], result[-1][i] = result[-1][i], result[-1][j]
        return result
