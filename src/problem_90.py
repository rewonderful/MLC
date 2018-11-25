#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def subsetsWithDup0( nums):
    """
    算法：递归/回溯
    思路：
        和第78题，求子集思路类似，但是不同的是这里要【去重】，以及【排序】

            n个元素的集合子集数目有2^n次方个，但是由于集合中有重复元素，所以实际的集合数目达不到这么多
        最直观的去重思想就是用set✅，但是要注意在python中，list对象是不能放到set中的，所以放到
        set中的应该是tuple元组类型，其实set只是辅助去重，所以在添加的时候，只要判断tuple()后的
        元组是否在set中就可以了，不在的话，就可以添加到result的中，否则的话就不添加，当然了，同时
        也要更新set，也可以不用result直接用set最后将set转为list也ok，但是这样和直接用list类型的
        result相比算是用空间换时间吧

            这里要注意使用递归生成所有子集的时候要先把原来的数组进行排序后再进行递归，如果不进行排序的
        话，(2,1,2)与(1,2,2)将被视为是两个不同的子集，但是事实上二者是同一个子集，将数组排序后
        进行子集的生成可以延续78题中一个个子集元素是按层自上而下添加进去的思想。

    复杂度分析：
        时间：O2^N，实际上遍历了所有O2^N个子集（也是O2^N种可能的情况），只不过重复集合不添加罢了
        空间：O2^N，递归栈空间以及存储子集的result，res_set的空间
    """
    def generate(i, nums, subset, result, res_set):
        if i >= len(nums):
            return
        generate(i + 1, nums, subset[:], result, res_set)
        subset.append(nums[i])
        if tuple(subset) not in res_set:
            result.append(subset)
            res_set.add(tuple(subset))
        generate(i + 1, nums, subset[:], result, res_set)

    nums.sort()
    result = [[]]
    generate(0, nums, [], result, set())
    return result
def subsetsWithDup1( nums):
    """
    与78题中的二进制解法类似，只是这里也添加了【排序】和【set去重】的步骤

    """
    nums.sort()
    all_set = 1 << len(nums)
    result = []
    res_set = set()
    for i in range(all_set):
        subset = []
        for j in range(len(nums)):
            # 或者1<<(len(nums)-1-j) & i
            if 1 << j & i:
                subset.append(nums[j])
        if tuple(subset) not in res_set:
            result.append(subset)
            res_set.add(tuple(subset))
    return result
def subsetsWithDup2( nums):
    """
    与78题中的二进制解法类似，只是这里也添加了【排序】和【set去重】的步骤
    """
    nums.sort()
    res_set = set()
    ans = [[]]
    for num in nums:
        for exist in ans[:]:
            tmp = [num]+exist
            if tuple(tmp) not in res_set:
                ans.append(tmp)
                res_set.add(tuple(tmp))
    return ans
if __name__ == '__main__':
    print(subsetsWithDup2([2,1,2]))
