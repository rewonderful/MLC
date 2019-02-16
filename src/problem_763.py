#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def partitionLabels(S):
    """
    算法：贪心，双指针
    思路：
        记录每个字母的最后出现的位置，再遍历整个字符串，用一个指针start和end记录当前区间的起止位置，
        目标区间应该是能使得区间内的所有字母都只出现在区间内的最短的区间，
        所以再遍历一次S，设置end = max(end, last[char]),当前位置 == end时，就说明一段区间已经
        添加完了，ans append进去，更新start为end + 1 为下一区段的开始处

        说是贪心就是因为是处理完一小段再处理一小段，前后还没关系
    """
    last = {char: position for position, char in enumerate(S)}
    start = end = 0
    ans = []
    for position, char in enumerate(S):
        end = max(end, last[char])
        if position == end:
            ans.append(end - start + 1)
            start = end + 1
    return ans