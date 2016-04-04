#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def moveZeroes_1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        for i in range(j, -1, -1):
            if not nums[i]:
                while i < j:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    i += 1
                nums[j] = 0
                j -= 1

    def moveZeroes_2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_total = nums.count(0)
        for i in range(zero_total):
            nums.remove(0)
        nums.extend([0] * zero_total)

    def moveZeroes_3(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


"""
if __name__ == '__main__':
    Solution().moveZeroes_2([0, 0, 1])
"""
