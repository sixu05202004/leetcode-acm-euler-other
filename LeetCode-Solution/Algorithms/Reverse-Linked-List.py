#!/usr/bin/env python
# -*- coding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        elif not head.next:
            return head
        p1, p2, p3 = head, head.next, head.next.next
        while p1 and p2:
            if p1 == head:
                p1.next = None
            p2.next = p1
            if p3:
                p1, p2, p3 = p2, p3, p3.next
            else:
                p1, p2, p3 = p2, p3, None
        return p1
