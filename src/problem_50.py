#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    """
    solution method
    把x的n次方分解为 n/2 n/2,
    要注意的是，n可能会小于0 ，所以在一开始有一个对小于0的n的操作

    还要注意后面分解为return self.myPow(x * x, n // 2)，这样避免了数值溢出，事实上这就是两种写法，也可以写成
    return self.myPow(x, n // 2) ** 2，但是这样计算会报错（我也不晓得为啥）

    """
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n // 2)
