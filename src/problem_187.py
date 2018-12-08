#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findRepeatedDnaSequences( s):
    """
    算法：哈希表
    思路：
        遍历所有10一组的DNA序列，记录所有序列出现的次数，超过1次的添加到集合中，最后返回集合内元素
    复杂度分析：
        时间：ON，遍历一次所有DNA序列
        空间：ON哈希表空间
    """
    if len(s) < 10:
        return []
    count_map = {}
    result = set()
    for i in range(10, len(s) + 1):
        DNA = s[i - 10:i]
        count_map.setdefault(DNA, 0)
        count_map[DNA] += 1
        if count_map[DNA] > 1:
            result.add(DNA)
    return list(result)
if __name__ == '__main__':
    print(findRepeatedDnaSequences('AAAAAAAAAAA'))
