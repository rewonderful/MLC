#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def longestConsecutive(self, nums):
    """
    Solution Method
    算法：集合
    思路：
        其实题解的思路挺朴素的，就是将nums转化为集合，然后使得查找时间退化为O1
            只在nums中对每个num做序列起始位置的情况进行查找，然后用while一直从起始位置开始向后探索，
        其实对比于下面我的方法，这样做最起码避免了我的那种一个序列中每个位置都要计算的问题，只从开头进行
        探索，会快很多
    """
    num_set = set(nums)
    ans = 0
    for num in nums:
        if num - 1 in num_set:
            continue
        curr = num + 1
        curr_longest = 1
        while curr in num_set:
            curr_longest += 1
            curr += 1
        ans = max(ans, curr_longest)
    return ans
def longestConsecutiveX(self, nums):
    """
    My TLE Method
    过了66/68个case，最后TLE了，TLE的原因应该就在于向上探索的while和向下探索的while
        我这里用的思路有点像并查集的意思，比如现在来了个数字3，如果记record[3] = 1，然后分别
    向上num+1 和向下num-1去记录向上向下的最大的连续字段，相当于看看3的上面一团最大是多少比如是
    连续的5个，3的下面一团最大的是多少，比如是连续的3个，那么3加进来后就是上面的加下面的再加当前
    的这1个3，包含3的最大连续字段就是5+3+1，这样的问题就在于，一个是上下while求某一侧一团数字的max
    时要遍历两次，再一个是我这对每一个最大序列中的任何一个位置都求了一次上下最大团的个数，有点浪费时间
    """
    record = dict()
    ans = 0
    for num in nums:
        if num in record and record[num] != 0:
            continue
        record[num] = 1
        sub_max = 0
        sub = num - 1
        while sub in record and record[sub] != 0:
            sub_max = max(sub_max, record[sub])
            sub = sub - 1
        top = num + 1
        top_max = 0
        while top in record and record[top] != 0:
            top_max = max(top_max, record[top])
            top = top + 1
        record[num] += (top_max + sub_max)
        if num - 1 not in record:
            record[num - 1] = 0
        if num + 1 not in record:
            record[num + 1] = 0
        ans = max(ans, record[num])

    return ans
if __name__ == '__main__':
    print(longestConsecutive([1,2,0,1]))