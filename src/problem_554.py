#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def leastBricks(self, wall: 'List[List[int]]') -> 'int':
    """
    算法：哈希表
    思路：
        遍历每一行，记录下来每一行中的每个缝隙处的个数，最终答案应该是行数减去最多计数的缝隙数

        要注意的是每一行中的最后一个砖头不能加上，因为根据题意，最开始的缝隙和最末的缝隙是不能
        算在里面的。所以遍历的时候是 for width in row[:-1]
    """
    if len(wall) == 0:
        return 0

    record = {}
    max_gap = 0
    for row in wall:
        left = 0
        for width in row[:-1]:
            left += width
            record.setdefault(left, 0)
            record[left] += 1
            max_gap = max(max_gap, record[left])
    return len(wall) - max_gap