#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        curr = 1
        ans = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
                ans = max(ans,curr)
            else:
                curr = 1
        return ans