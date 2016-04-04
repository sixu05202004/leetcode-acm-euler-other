#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
             'X': 24, 'Y': 25, 'Z': 26}
        char_list = list(s)
        char_list.reverse()
        sum_value = 0
        for i in range(len(char_list)):
            if i == 0:
                sum_value += d.get(char_list[i])
            else:
                sum_value += d.get(char_list[i]) * (26**i)
        return sum_value

    def titleToNumber_anthor(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
             'X': 24, 'Y': 25, 'Z': 26}
        s_len = len(s)
        sum_value = 0
        for i in range(s_len):
            pow_n = s_len - i - 1
            if not pow_n:
                sum_value += d.get(s[i])
            else:
                sum_value += d.get(s[i]) * (26**pow_n)
        return sum_value
