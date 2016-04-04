#!/usr/bin/env python
# -*- coding: utf-8 

"""
题目的中文含义大概是：
你和小伙伴玩游戏，从一堆石头里面每次可以拿出来一个到三个之间，谁最后拿完石头谁赢。你现在是第一个拿石头的，能不能找最优的策略，保证你能赢得局全部拿下，赢不了的那就没办法了。 

"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4!=0