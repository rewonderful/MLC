#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def searchRange7(nums, target):
    """
    :param nums:
    :param target:
    :return:
    用二分查找去找到最左侧的left，
    用二分查找再去找到最右侧的right
    要注意的是，和二分查找不一样的地方是返回条件不一样了
    比如二分查找左侧，
    当nums[mid] == target时，由于左侧还可能有target，所以r = mid -1 ，而且最后返回的是l
    因为如果左侧再没有target后，那么左侧的值其实就是一只小于target的，就会l一直++，知道l>r，刚好是最前面的
    那个target的位置
    右侧二分查找同理
    """
    def binarySearchLeft(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def binarySearchRight(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return r

    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]
def searchRange0( nums, target):
    """
    My Method_v3
    算法：二分查找
    思路：
           用二分查找找两次target，一次在查找start，一次查找end
            每次查找的框架和二分查找相差无几，关键在于由于元素会有多个重复，也就是说当num[mid]==targt时
        的mid不一定是我们要查找的左右端点。所以要添加左右端点的限制
        在nums[mid] == target的前提下
            左端点的特点是要么左端点mid==0，要么nums[mid-1] <target，满足该条件的就是左端点，可以
            记录在position中，并且后续对右端点的查找从左端点开始，可以节省时间
            右端点类似，要么是右端点mid == len(nums)-1，要么是nums[mid+1] > target，满足该条件的
            就是右端点，可以记录在position中，break然后return
            要注意的是
                如果当前端点不是左端点或者右端点，那么该怎么办？很明显，如果在找左端点的过程中
            nums[mid]==target但是它不是左端点，那么就应该将hi设置为mid-1,从左半段开始寻找，并且continue直接
            开始下一次。寻找右端点的过程类似，lo = mid + 1，并且直接continue
    复杂度分析：
        时间：OlogN,两遍二分查找，2个OlogN，和为OlogN
        空间：O1，常数级
    """
    position = [-1, -1]
    lo = 0
    hi = len(nums) - 1
    start = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] < target:
                position[0] = mid
                start = mid
                break
            else:
                hi = mid - 1
                continue
        if target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    lo = start
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] > target:
                position[1] = mid
                break
            else:
                lo = mid + 1
                continue
        if target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return position
def searchRange1(self, nums, target):
    """
    My Method_v1
    算法：朴素遍历
    思路：
            很朴素的想法，一个for循环遍历所有的元素，由于已经排序过了， 初始化position为[-1,-1]，第一次遍历到
        的时候，就将position设置为[i,i],不设置为[i,-1]是因为可能整个nums只有这一个元素所以直接将position变成
        [i，i]就好，后面再找到的时候不论找到多少次，都只更新position[1]=i，即更新末尾位置
            由于是排序过的数组，所以当nums[i] > target时，直接break,降低时间复杂度
    复杂度分析：
        时间：ON，一次遍历
        空间：O1，常数级
    """
    position = [-1, -1]
    for i in range(len(nums)):
        if nums[i] > target:
            break
        if nums[i] == target:
            if position[0] == -1:
                position = [i, i]
            else:
                position[1] = i

    return position

def searchRange2( nums, target):
    """
    My Method_v2
    算法："暴力"二分
    思路：
        二分查找到target后左右分别遍历到左端点和右端点
    复杂度分析：
        时间：O(NlogN)，二分查找OlogN，遍历两个ON，故NlogN
        空间：O(1)，常数级
    """
    position = [-1, -1]
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            position = [mid, mid]
            left_hi = mid - 1
            right_lo = mid + 1
            while left_hi >= 0 and nums[left_hi] == target:
                position[0] = left_hi
                left_hi -= 1
            while right_lo <= len(nums) - 1 and nums[right_lo] == target:
                position[1] = right_lo
                right_lo += 1
            break
        if target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return position



if __name__ == '__main__':
    print(searchRange7([5,7,7,8,8,10],8))

