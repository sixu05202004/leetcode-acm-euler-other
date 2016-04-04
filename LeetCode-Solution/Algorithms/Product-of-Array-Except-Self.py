#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def productExceptSelf_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        这个解决方案不符合题目要求
        """
        total = 1
        flag = 0
        if nums.count(0) == 1:
            for i in nums:
                if i:
                    total *= i
            flag = 1
        else:
            total = reduce(lambda x, y: x * y, nums)
        for i in range(len(nums)):
            if nums[i] and flag:
                nums[i] = 0
            elif nums[i] and not flag:
                nums[i] = total / nums[i]
            else:
                nums[i] = total
        return nums

    def productExceptSelf_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp_l = [nums[0]]
        t = 1
        for i in range(1, len(nums)):
            temp_l.append(nums[i] * temp_l[i - 1])
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                nums[i] = t
                break
            temp = nums[i]
            nums[i] = temp_l[i - 1] * t
            t = t * temp
        return nums
