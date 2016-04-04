#!/usr/bin/env python
# -*- coding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        tail = pre = head
        exist_value = {}
        while head:
            if exist_value.get(head.val) is not None:
                pre.next = head.next
                head = pre.next
            else:
                exist_value[head.val] = head.val
                pre = head
                head = head.next
        return tail
