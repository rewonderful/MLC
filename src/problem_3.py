#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# def lengthOfLongestSubstring(s): #解法1，两层for，n2的复杂度，800+ ms
#     """
#     :type s: str
#     :rtype: int
#     """
#     if len(s) ==0:
#         return 0
#     max = 1
#     for i in range(len(s)):
#         char = s[i]
#         tmp = set(char)
#         count = 1
#         for j in range(i+1,len(s)):
#             char_next = s[j]
#             if char_next not in tmp:
#                 tmp.add(char_next)
#                 count += 1
#             else:
#                 break
#             max = count if count > max else max
#
#     return max
def lengthOfLongestSubstring2(s): #108ms  要用内置函数max会更快！
    if s == '':
        return 0
    queue = list()
    one_max = 1
    for char in s:
        if char not in queue:
            queue.append(char)
        else:
            length = len(queue)
            one_max = max(length, one_max)
            queue = queue[queue.index(char) + 1:]
            queue.append(char)
    final_len = len(queue)
    one_max = max(final_len, one_max)
    return one_max

if __name__ == '__main__':
    #print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring2("dvdf"))




