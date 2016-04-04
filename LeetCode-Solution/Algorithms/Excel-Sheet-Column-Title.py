#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def titleToNumber(self, n):
        """
        :type n: int
        :rtype: str
        """
        d = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W',
             24: 'X', 25: 'Y', 26: 'Z'}
        outstr = []
        while n >= 1:
            outstr.append(d[n % 26])
            if not n % 26:
                n = n / 26 - 1
            else:
                n = n / 26
        outstr.reverse()
        return ''.join(outstr)
