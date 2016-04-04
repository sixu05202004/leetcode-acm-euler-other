#!/usr/bin/env python
# -*- coding: utf-8

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution(object):

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        queue = []
        queue.append((root, 1))
        while queue:
            node_pairs = queue.pop(0)
            node, level = node_pairs[0], node_pairs[1]

            if not queue or queue[0][1] != level:
                node.next = None
            else:
                node.next = queue[0][0]
            if node.left:
                queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
