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
        nums_dict = {}
        for i in nums:
            if not nums_dict.get(i):
                nums_dict[i] = 1
            elif nums_dict.get(i) and nums_dict.get(i) < 2:
                nums_dict[i] += 1
            else:
                nums.remove(i)

        return len(nums), nums_dict, nums

if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 1, 1])
