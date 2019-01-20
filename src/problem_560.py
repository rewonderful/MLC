#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def subarraySum(nums, k):
    """
    Inspired By Hint
    算法：哈希表
    思路：
        首先可以把最暴力的解法写出来，用三层for 遍历一个一个子序列，这样明显有冗余
        可以稍微改进，用两层for 来遍历，用一个sum记录前面的累加和，再记录sum += nums[i]加当前的就好了

        下面这个是ON的做法，因为sum(i,j) = sum(0:j)-sum(0:i),所以可以在一次遍历中，记录0：i的sum值
        并且用hash表存储起来，就像two sum 一样，如果当前和是3，目标是10，那么就期望后面有一刻和是13，即
        key = curr_sum+k,代表着需要这个key的值的前序有多少个子序列，所以如果某次遍历中curr_sum in hash_map
        的话，就counter += hash_map[key].
    复杂度：
        时间：ON
        空间：ON
    """
    counter = 0
    hash_map = {k: 1}
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum in hash_map:
            counter += hash_map[curr_sum]
        hash_map.setdefault(curr_sum + k, 0)
        hash_map[curr_sum + k] += 1
    return counter
if __name__ == '__main__':
    print(subarraySum([1,2,3],3))