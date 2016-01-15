#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Bruce Chen'

'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

from functools import reduce
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = []
        for k in list(range(rowIndex+1)):
            if k == 0 or k == rowIndex:
                num = 1
            else:
                num = reduce(lambda x,y:x*y, range(rowIndex+1-k,rowIndex+1))//reduce(lambda x,y:x*y, range(1,k+1))
            l.append(num)
        return l

c = Solution()
a = c.getRow(6)
print(a)





