#!/usr/bin/env python
# -*- coding: utf-8


class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_set, t_set, s_dict, t_dict = set(s), set(t), {}, {}
        for i in s_set:
            s_dict[i] = s.count(i)
        for i in t_set:
            t_dict[i] = t.count(i)
        return s_dict == t_dict
