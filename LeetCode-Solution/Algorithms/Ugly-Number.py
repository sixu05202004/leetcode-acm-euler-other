#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        elif num == 1:
            return True
        elif num % 2 and num % 3 and num % 5:
            return False
        else:
            while not num % 2:
                num = num / 2
            while not num % 3:
                num = num / 3
            while not num % 5:
                num = num / 5
            if num == 1:
                return True
            else:
                return False
