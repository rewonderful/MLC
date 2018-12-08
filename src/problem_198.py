#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def rob(nums):
    """
    算法：动规
    思路：
        思路比较直观，转化为动规去做
        最优子结构：
                假设现在判断第5个位置
                抢还是不抢取决于gain[3]+nums[5]和gain[4]哪个大，即当前最优解由更小的子问题构造
        重叠子问题：
                gain[5]取决于gain[4],gain[3]
                gain[4]取决于gain[3],gain[2]
                ...
        对于第i个位置，有抢或者不抢两种选择
            如果不抢的话，当前gain[i] = gain[i-1]
            如果抢的话，当前gain[i] = gain[i-2] + nums[i]
        所以gain[i] = max(gain[i - 2] + nums[i], gain[i - 1])
        这即是状态转移方程
        边界条件：当i = 0时，显然最大值就是nums[0]，i=1时，最大值就是max(nums[0],nums[1])
    复杂度分析：
        时间：ON，遍历一遍
        空间：ON，gain的空间
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    gain = [0] * len(nums)
    gain[0] = nums[0]
    gain[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        gain[i] = max(gain[i - 2] + nums[i], gain[i - 1])
    return gain[-1]
if __name__ == '__main__':
    print(rob([1,2,3,1]))