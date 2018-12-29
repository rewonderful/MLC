#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findDisappearedNumbers( nums):
    """
    算法：
    思路：
        我原来看完Disscussion后选择的标记方式是标记为-1，如下面👇的解法，但是这样空间就是ON了
        所以考虑用原数组本身做mark记录，那么为什么下面的方法中我要用一个额外的mark数组记录？
        因为如果用原数组，很容易使得正在遍历的数组自身的值发生改变，影响后序遍历，比如原来数组是[5,4,3,2,1]
        遍历半中间我变成了[5,4,-1,2,1]那遍历到i=2的时候，nums[i] = -1了，这显然有问题。所以为了要保持
        原数组的可索引性，要更改标记的方式，令标记nums[i] = - abs(nums[i])就OK了，这样在索引的时候只要再abs(nums[i])-1
        即可恢复争取的索引，反正mark一下只是想做个标识，只要能区分正负来标记是否访问过就好了！
    """
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]

def findDisappearedNumbers1(self, nums):
    """
    My Mark Method
    用一个辅助数组mark来记录访问过的元素，但是这样会增加ON的空间
        因为元素是从1到n的，所以可以用nums[i]-1做下标index去标记访问情况，我这里将访问过的位置标记为-1，最后遍历
    没有被标记过的位置不就是要求的结果。
    """
    mark = nums[:]
    for i in range(len(nums)):
        index = nums[i] - 1
        mark[index] = -1
    return [i + 1 for i in range(len(mark)) if mark[i] > 0]
if __name__ == '__main__':
    print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))