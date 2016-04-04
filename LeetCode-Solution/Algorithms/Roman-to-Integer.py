#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                             'C': 100, 'D': 500, 'M': 1000, '0': 0}
        return sum([romanDict[c] if romanDict[c] >= romanDict[d] else romanDict[c] * -1 for c, d in zip(s, (s + '0')[1:])])
