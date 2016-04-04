#!/usr/bin/env python
# -*- coding: utf-8


class Solution_1(object):
    # 最基本的方法

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            strnum = str(num)
            result = 0
            for i in strnum:
                result += int(i)
            return self.addDigits(result)


class Solution_2(object):
    # 根据数根公式 b = ( a - 1) % 9 + 1 计算

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return num
        return (num - 1) % 9 + 1
