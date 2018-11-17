#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def titleToNumber(self, s):
    """
    算法：
        列几个例子就可以发现，AB实际上就是26+2，AZ是26+26，其实就是从右边来看，最右边的字母转数字时，是26的0次方
        从右往左第二位的底是26的1次方，ABC这样的数其实其底分别是26^2,26^1,26^0，所以将字母转数字后乘对应的底并相加即可
    复杂度分析：
        时间On：扫描一遍字符串
        空间O1：ans等常数级辅助存储空间
    """
    length = len(s)
    ans = 0
    for i in range(length):
        ans += (26 ** (length - i - 1)) * (ord(s[i]) - 64)
    return ans