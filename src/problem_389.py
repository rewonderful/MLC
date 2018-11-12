#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findTheDifference(self, s, t):
    """
    分析：
        新的字符串是在原字符串基础上生成的，因此两个字符串一定是有重叠的部分，也就意味着有的字符是出现2次的
        进而联想到136题的做法，用异或操作来找到数目为单个的元素
    算法：
        将字符串拼接，转化为ASCII码值进行异或运算，偶数次重复值将被异或运算为0，N^N=0，0^N=N，剩余的就是多余的字符
    复杂度分析：
        时间：On，字符串拼接O1,字符串转换ASCII列表On，异或运算遍历On
        空间：On，字符串转换ASCII列表On
    """
    st = ''.join([s, t])
    st_ord = []
    for char in st:
        st_ord.append(ord(char))
    bit = 0
    for num in st_ord:
        bit ^= num
    return chr(bit)
def findTheDifference_count(self, s, t):
    """
    算法：
        计算26字母每个字符串对每个字母的频次，不相等的那个字母就是多余的字母
    复杂度分析：
        空间：O1
        时间：~，至少On，遍历所用，但是不清楚count的用时，count可能为On，则耗时On2
    """
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(c) != t.count(c):
            return c