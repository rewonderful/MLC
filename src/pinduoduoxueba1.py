#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def calculate_varience(nums):
    if len(nums) < 3:
        return float("inf")
    mean = sum(nums)/len(nums)
    var = 0
    for num in nums:
        var += (num-mean)**2
    var = round(var/3,2)
    print(var)
    return var

def solution1(nums):
    nums.sort()
    ans = float("inf")
    for i in range(len(nums)):
        ans = min(ans,calculate_varience(nums[i:i+3]))


    return ans

if __name__ == '__main__':

    #n = int(input())
    #nums = list(map(int,input().strip().split()))

    print(solution1([10,17,17,3]))
