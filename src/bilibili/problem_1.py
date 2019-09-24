#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solution(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if int(nums[i]+nums[j]) < int(nums[j]+nums[i]):
                nums[i],nums[j] = nums[j],nums[i]

    ans = ''.join(nums)
    ans = ans.lstrip('0')
    return ans if ans else '0'
    #nums.sort(key=lambda x,y:1 if int(x+y)>=int(y+x) else -1 ,reverse=True)



if __name__ == '__main__':
    nums = list(input().strip().split (','))
    #nums = ["1","30"]
    print(solution(nums))