#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

if __name__ == '__main__':
    import random
    nums = [random.randint(1,100)  for _ in range(20)]
    #print(nums  )
    print(bubbleSort([10,9,8,7,6,5,4,3,2,1,]))