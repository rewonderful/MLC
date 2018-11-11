#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() #数组题不好想的时候可以考虑先排序一下再做
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):  # 因为下一个数如果和自己相等的话，这次求解时已经一定会把下一个数的解囊括进来了
                target = -nums[i]
                low = i + 1
                high = len(nums) - 1
                while (low < high):
                    if nums[low] + nums[high] == target:
                        res.append([nums[i], nums[low], nums[high]])
                        while (low < high and nums[low] == nums[low + 1]): low += 1   #当前求解后，low high都应该移动，但是移动的时候要跳过重复值
                        while (low < high and nums[high] == nums[high - 1]): high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < target:
                        low += 1
                    else:
                        high -= 1
        return res
    