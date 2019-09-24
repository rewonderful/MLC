#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def get_least_operations(n,m,nums):
    cnt = 0
    min_nums = []
    for i in range(n-1):
        min_nums.append(min(nums[i+1:]))
    min_nums.append(nums[-1])
    flag = False
    for i in range(n):
        if min_nums[i] < nums[i]:
            cnt += nums[i] - min_nums[i]
            flag = True
        elif i >= 1 and nums[i] >= nums[i-1]:
            if flag:
                cnt += nums[i] - nums[i-1]
            else:
                flag = False
    return cnt
if __name__ == '__main__':
    n,m = list(map(int,input().strip().split()))
    nums = list(map(int,input().strip().split()))
    print(get_least_operations(n,m,nums))