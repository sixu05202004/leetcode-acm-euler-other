#!/usr/bin/env python
# -*- coding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left = 1
        right = 1
        left += self.maxDepth(root.left)
        right += self.maxDepth(root.right)
        return left if left > right else right
