#!/usr/bin/env python
# -*- coding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def rsortedArrayToBST(self, array, start, end):
        if start > end:
            return
        mid = (start + end) / 2
        root = TreeNode(array[mid])
        root.left = self.rsortedArrayToBST(array, start, mid - 1)
        root.right = self.rsortedArrayToBST(array, mid + 1, end)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        return self.rsortedArrayToBST(nums, 0, len(nums) - 1)
