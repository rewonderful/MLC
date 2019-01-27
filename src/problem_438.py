#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findAnagrams(self, s, p):
    """
    My Method
    滑动窗口
    用哈希表记录滑动窗口内的字符个数，如果滑动窗口内的sub_hash  == pattern，则找到一个
    滑动窗口的left 就是i，right就是i+len(p)-1
    关键就在于避免重复计算，所以在窗口右移的过程中，left向右一位，所以原来left指向的key值-=1，如果
    那个key对应的v == 0，就pop这个key
    然后右移的时候新纳入的right，计数值+ 1
    """
    result = []

    pattern = {}
    for char in p:
        pattern.setdefault(char, 0)
        pattern[char] += 1
    i = 0
    sub_hash = {}
    while i < len(s) - len(p) + 1:

        if len(sub_hash) == 0:
            substring = s[i:i + len(p)]
            for char in substring:
                sub_hash.setdefault(char, 0)
                sub_hash[char] += 1
        else:
            sub_hash[s[i - 1]] -= 1
            if sub_hash[s[i - 1]] == 0:
                sub_hash.pop(s[i - 1])
            sub_hash.setdefault(s[i + len(p) - 1], 0)
            sub_hash[s[i + len(p) - 1]] += 1

        if sub_hash == pattern:
            result.append(i)
        i += 1

    return result