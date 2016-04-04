#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        iscarry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                if digits[i] + 1 < 10:
                    digits[i] = digits[i] + 1
                    return digits
                else:
                    digits[i] = digits[i] - 9
                    iscarry = 1
            else:
                if digits[i] + iscarry < 10:
                    digits[i] = digits[i] + iscarry
                    return digits
                else:
                    digits[i] = digits[i] + iscarry - 10
                    iscarry = 1
        if not iscarry:
            return digits
        else:
            return [iscarry] + digits
