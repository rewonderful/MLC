#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def calculate( s):
    """
    Disscussion Method
    算法:栈
    思路：
        遍历字符串，将一串式子看成是各种乘除法计算后式子的和
        如"1*2-3/4+5*6-7*8+9/10"
        可以看成 1*2 + -3/4 + 5*6 + -7*8 + 9/10

        也就是说当检测到数字(一个完整的数字，如10,)时
        根据这个数字前的运算符，如果是加号，就直接入栈，如果是减号入栈 -num
        如果是乘号，将栈顶弹出 top*num，再将运算结果压栈
        如果是除号，将栈顶弹出，根据栈顶top的正负号再运算一波，然后将运算结果入栈

        如果不是数字且不是空格，那么就是运算符了。op=新的运算符更新
    复杂度：
        时间：ON
        空间：ON
    """
    stack = []
    op = '+'
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = 10 * num + ord(s[i]) - ord('0')
                i += 1
            if op == '+':
                stack.append(num)
            if op == '-':
                stack.append(-num)
            if op == '*':
                stack.append(num * stack.pop())
            if op == '/':
                tmp = stack.pop()
                if tmp < 0:
                    stack.append(-(-tmp//num))
                else:
                    stack.append(tmp//num)
            continue
        elif s[i] != ' ':
            op = s[i]
        i += 1
    return sum(stack)
if __name__ == '__main__':
    print(calculate("1*2-3/4+5*6-7*8+9/10"))