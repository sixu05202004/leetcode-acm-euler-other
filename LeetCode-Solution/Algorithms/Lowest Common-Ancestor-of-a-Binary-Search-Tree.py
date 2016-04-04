#!/usr/bin/env python
# -*- coding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        result = root
        while result:
            if result.val > p.val and result.val > q.val and result.left:
                result = result.left
                continue
            elif result.val < p.val and result.val < q.val and result.right:
                result = result.right
                continue
            break
        return result
