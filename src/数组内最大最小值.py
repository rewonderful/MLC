#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random
# def reduce(pair):
#     if len(pair) == 1:
#         return [pair[0],pair[0]]
#     else:
#         if pair[0] < pair[1]:
#             pair[0],pair[1] = pair[1],pair[0]
#         return pair
def find_max_min(nums):

    max_num = float('-inf')
    min_num = float('inf')
    for i in range(0,len(nums),2):
        #pair = reduce(nums[i:i+2])
        pair = nums[i:i+2]
        if len(pair) == 1:
            pair = [pair[0], pair[0]]
        elif pair[0] < pair[1]:
                pair[0], pair[1] = pair[1], pair[0]
        max_num = max(max_num,pair[0])
        min_num = min(min_num,pair[1])
    return max_num,min_num

if __name__ == '__main__':
    n = 100000
    nums = [ random.randrange(n) for _ in range(n//2)]
    print(find_max_min(nums))
    print(max(nums),min(nums))