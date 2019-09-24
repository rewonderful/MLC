#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solution(nums):
    if len(nums) == 1:
        return 0
    if len(nums) == 0:
        return 0
    dp = [-1] * len(nums)
    dp[0] = 0
    for i in range(1,len(dp)):
        smallest_index = i
        for j in range(i):
            if j + nums[j] >= i and j < smallest_index :
                smallest_index = j
        if smallest_index < i:
            dp[i] = dp[smallest_index] + 1
        if i == smallest_index == len(nums)-1:
            return -1
    return dp[-1]


    # ans = 0
    # i = 0
    # while i < len(nums)-1:
    #     next_step = nums[i]
    #     biggest = 0
    #     biggest_index = 0
    #     for j in range(i+1,i+next_step+1):
    #         if j < len(nums) and nums[j] >= biggest and nums[j] != 0:
    #             biggest = nums[j]
    #             biggest_index = j
    #     i = biggest_index
    #     ans += 1

    #return ans


if __name__ == '__main__':
    nums = [2, 2, 3, 0, 4]
    print(solution(nums))