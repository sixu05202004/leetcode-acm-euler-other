#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for i in nums:
            result[i] = result.get(i, 0) + 1
        max_nums = 0
        max_element = 0
        for (k, v) in result.items():
            if v > max_nums:
                max_nums = v
                max_element = k
        return max_element

    def majorityElement_another(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        len_t = len(nums) // 2
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] > len_t:
                return num
