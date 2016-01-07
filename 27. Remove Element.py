#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Bruce Chen'

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return None
        while val in  nums:
            nums.remove(val)

        return len(nums)


c=Solution()
a=c.removeElement([1,2,2,3,4],2)
print(a)