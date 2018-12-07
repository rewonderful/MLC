#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def longestPalindrome(s):
    """
    和MyMethod类似，但是奇数频次的处理方式更佳！
        将奇数都按偶数存进去，最后补一个中间节点就好了!abba补为ababa，表现在longsest上就是+1
        所以在后面累加的时候，奇数都-1变成偶数加进去，并且设一个flag，如果有奇数，flag =1 ，最后longest补个1就好
    """
    record = {}
    for c in s:
        record.setdefault(c, 0)
        record[c] += 1
    longest = 0
    ifodd = 0
    for _, count in record.items():
        if count % 2 == 0:
            longest += count
        else:
            longest += count - 1
            ifodd = 1

    return longest + ifodd
def longestPalindrome1( s):
    """
    My Method
    算法：哈希表
    思路：
        哈希表记录所有字符出现的频次
        最大回文串的长度就是所有偶数频次的和加奇数频次处理后的和
            可以将奇数频次-=1 转化为偶数频次，但是不能简单的全部都-=1，如'ccc'，奇数频次为3，
        最大长度就是3，而不是2，我这里处理的方式是将所有奇数频次都-1后加进去，然后如果奇数个数
        大于1的话，每个奇数都-1，但是有一个奇数不用-1，所以是sum(jishu) - (len(jishu) - 1)，
        如果只有一个奇数的话，直接+这个奇数值就好
    复杂度分析：
        时间：ON，遍历，sum
        空间：ON，哈希表空间
    """
    record = {}
    for c in s:
        record.setdefault(c, 0)
        record[c] += 1
    longest = 0
    jishu = []
    for _, count in record.items():
        if count % 2 == 0:
            longest += count
        else:
            jishu.append(count)
    longest += sum(jishu) - (len(jishu) - 1) if len(jishu) > 1 else sum(jishu)

    return longest
if __name__ == '__main__':
    print(longestPalindrome('abccccdd'))