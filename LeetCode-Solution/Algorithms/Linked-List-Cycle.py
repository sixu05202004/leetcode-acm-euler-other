#!/usr/bin/env python
# -*- coding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        node_list = {}
        p = head
        result = False
        while p:
            if node_list.get(p):
                result = True
                break
            else:
                node_list[p] = 1
                p = p.next
        return result
