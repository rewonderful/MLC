#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#ref:https://segmentfault.com/a/1190000008824222
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_height = 0
        while(left < right):
            max_height = max(max_height,min(height[left],height[right]) * (right - left))
            if height[left] < height[right]:
                left +=1
            else:
                right -= 1
        return max_height