#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def calculate(self, s):
    """
    Disscussion Method
    算法：栈
    思路：
        输入一共就6种可能
        0123456789
        (
        )
        +
        -
        _ 空格
        所以其实只要对这几种情况分别进行判断就好了，其中空格可以不用管，直接省略过去

        操作符可以用+1与-1来代表加号减号的操作

            用一个栈来保存前序的计算结果，当遇到左括号的时候，将目前序列计算得到的结果ans和括号前的操作符op
        入栈(ans,op)，因为接下来要算括号内的结果了，所以要置括号内的初始操作符为op = +1，即加号，并置ans = 0

        (👆这样建立的栈充分体现了使用栈的目的是暂存运算中间状态)

        遇到右括号的话，当前ans计算的括号内的元素结果运算完毕，stack pop，将前序结果出栈，包括运算符，然后
        更新当前运算结果。
            ans *= op
            ans += pre,
        然后继续向后遍历
        注意当目前指向的字符是数字的话，要用while获得整个完整的数字
    复杂度分析:
        时间：ON
        空间：ON
    """
    stack = []
    ans = 0
    op = 1
    i = 0
    while i < len(s):
        if s[i].isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            num = s[start:i]
            ans += (op * int(num))
            continue
        elif s[i] == '(':
            stack.append((ans, op))
            op = 1
            ans = 0
        elif s[i] == ')':
            pre, op = stack.pop()
            ans *= op
            ans += pre
        elif s[i] == '+':
            op = 1
        elif s[i] == '-':
            op = -1
        i += 1
    return ans
if __name__ == '__main__':
    print(calculate("1-(5)"))