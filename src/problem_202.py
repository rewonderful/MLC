#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def isHappy( n):
    """
    方法一：

    建立一个集合set来将每次计算的结果add到里面，如果出现重复的话，说明已经出现了循环，那么可以停止
    如果和为1的话则为True
    这里注意如何计算一个整数各位数之和：从最后一位即"个位"数开始，每次将最后一个数平方，然后用n//10来去除
    最后一位，循环直到n除以10为0，即前方没有数字

    时间复杂度：  内侧while循环len(n)次，外侧循环到 return，其实和输入规模无关，是问题本身决定的复杂度
    空间复杂度：  辅助集合的大小，和输入规模无关，和问题本身有关
    """
    visited = set()
    while True:
        the_sum = 0
        while n > 0:
            the_sum += (n % 10) ** 2
            n = n // 10
        n = the_sum
        if n == 1:
            return True
        if n in visited:
            return False
        else:
            visited.add(n)
"""
    方法二：设置快慢指针
    
    可以像链表中一样设置快慢"指针"，一个早一步运算，另一个慢一步运算，如果存在循环（圈），则一定会相遇
    要注意这里的期望结果1，也是一种循环，所以当两个运算相等时判断是不是等于1就可以了
    
    可以把这类问题看成是一种状态机，像链表一般
        
"""
def getSquareSum(self, n):
    the_sum = 0
    while n > 0:
        the_sum += (n % 10) ** 2
        n = n // 10
    return the_sum

def isHappy(self, n):

    fast = self.getSquareSum(n)
    fast = self.getSquareSum(fast)
    slow = self.getSquareSum(n)

    while fast != slow:
        fast = self.getSquareSum(fast)
        fast = self.getSquareSum(fast)
        slow = self.getSquareSum(slow)

    return slow == 1
if __name__ == '__main__':
    n=92
    sum = 0
    while n >0:
        sum += (n % 10)**2
        n = n//10
    print(sum)