#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def check1(nums):
    is_single = False
    for num in nums:
        if num > 0 and num < 10:
            if is_single:
                return False
            else:
                is_single = not is_single
        else:
            if not is_single:
                return False
            else:
                is_single = not is_single
    return True

def check2(nums):
    if nums[0] < 10 and  nums[-1] < 10:
        for i  in range(1,len(nums)-1):
            num = nums[i]
            if num < 10:
                return False
        return True
    return False

def check3(nums):
    if nums[0] >= 10 and nums[-1] >= 10:
        for i in range(1, len(nums) - 1):
            num = nums[i]
            if num >= 10:
                return False
        return True
    return False

def solution(nums):
    ans = []
    for num_list in nums:
        if check1(num_list) or check2(num_list) or check3(num_list):
            ans.append("true")
        else:
            ans.append("false")
    return " ".join(ans)



if __name__ == '__main__':

    import sys
    # nums = [[1, 23, 3, 42, 3, 56],
    #         [44, 1, 5, 71, 9, 35]]
    # nums = [[10, 3, 5, 2, 7, 9, 4, 5, 6, 9, 98],
    #         [3, 31, 56, 4, 55, 74],
    #         [1, 34, 25, 67, 89, 32, 45, 16, 23]]
    nums = []
    for line in sys.stdin:
        a = list(map(int,line.strip().split(" ")))
        nums.append(a)
    print(solution(nums))


