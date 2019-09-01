#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def solution(nums):
    nums.sort()
    ans = 0
    help = set()
    for num in nums:
        if num not in help:
            help.add(num)
        else:
            tmp = num
            count = 0
            while tmp in help:
                tmp += 1
                count += 1
            ans += count
            help.add(tmp)
    return ans
if __name__ == '__main__':
    nums = list(map(int,input().strip().split(',')))
    print(solution(nums))

