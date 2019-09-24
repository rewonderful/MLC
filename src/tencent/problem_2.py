#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solution(n,nums):
    nums.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            x,y = nums[i],nums[j]
            if min(abs(x),abs(y)) >= min(abs(x+y),abs(x-y)) and max(abs(x),abs(y)) <= max(abs(x+y),abs(x-y)):
                ans += 1
    return ans

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().strip().split()))
    print(solution(n,nums))