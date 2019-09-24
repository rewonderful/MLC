#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solution(nums):
    n = len(nums)
    num_sum = sum(nums)
    if num_sum % n != 0 :
        return -1

    avg_num = num_sum / n
    ans = 0
    for apple in nums :
        if abs(apple-avg_num) %2 != 0 :
            return -1
        if apple > avg_num:
            ans  += apple-avg_num
    return ans



if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    print(int(solution(nums)//2))