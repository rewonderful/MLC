#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def checkInclusion(self, s1, s2):
    """
    滑动窗口，
    和438题一样，判断是不是"排列数"，其实就是判断Count那个字典是不是相等
    那么就在s2上维持一个len(s1)长的滑动窗口，用sub_hash记录各个字符的字符数，如果sub_hash和pattern
    一样，那么就找到了，到最后如果都没有找到，那么就return False
    """
    pattern = {}
    for char in s1:
        pattern.setdefault(char, 0)
        pattern[char] += 1
    i = 0
    sub_hash = {}
    while i < len(s2) - len(s1) + 1:

        if len(sub_hash) == 0:
            substring = s2[i:i + len(s1)]
            for char in substring:
                sub_hash.setdefault(char, 0)
                sub_hash[char] += 1
        else:
            sub_hash[s2[i - 1]] -= 1
            if sub_hash[s2[i - 1]] == 0:
                sub_hash.pop(s2[i - 1])
            sub_hash.setdefault(s2[i + len(s1) - 1], 0)
            sub_hash[s2[i + len(s1) - 1]] += 1

        if sub_hash == pattern:
            return True
        i += 1

    return False