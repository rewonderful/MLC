#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#和第15题思路类似，数组从i开始，然后从后面的i+1到-1去检索，并且能证明如果前面的已经遍历过了，后面的再遍历就是重复，所以i+1：-1就够了
#不一样的是在下面判断的时候，这里用的是距离，可以画一个数轴看一下，不论正负，由于已经排序过了，如果sum>target，就应该让sum小一点，反之应该让】
#sun大一点
#要再添加nums[i] != nums[i - 1] 之类的判断来保障移动的时候跳过了重复的元素
def threeSumClosest( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if nums == None:
        return target
    disstance = float('inf')
    ans = 0
    nums.sort()
    for i in range(len(nums) - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                triple_sum = nums[i] + nums[left] + nums[right]
                if abs(triple_sum - target) < disstance:
                    disstance = abs(triple_sum - target)
                    ans = triple_sum
                if triple_sum > target:
                    while (left < right and nums[right - 1] == nums[right]): right -= 1
                    right -= 1
                else:
                    while (left < right and nums[left + 1] == nums[left]): left += 1
                    left += 1
    return ans


if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    print(threeSumClosest(nums,target))