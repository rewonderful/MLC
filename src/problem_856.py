#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def scoreOfParentheses2(self, S: str) -> int:
    """
    :param self:
    :param S:
    :return:
    把问题转化，一个括号，肯定是由基础的()=1这样的括号组成的。所以可以相当于因式分解
    (()(())) ==> (()) + ((()))
    (()()) == > (()) +(())
    ()(()) == > () + (())
    所以对整个字符串扫描，用一个变量记录当前的未闭合的左括号数，左括号balance ++ 右括号balance--
    比如(()(())),当扫描到(()时，左括号比右括号多，这个时候就是不不平衡的
    那么ans += score ("(())" )
    而一个成对嵌套的完全括号分数也好说，就是2^(左括号数-1) = 2^(balance) = 1<<balance

    复杂度：
        时间ON
        空间O1
    """
    ans = 0
    balance = 0
    for i in range(len(S)):
        if S[i] == '(':
            balance += 1
        else:
            balance -= 1
            if S[i - 1] == "(":
                ans += 2 ** balance
    return ans
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        左括号，就塞0，右括号来的时候，看stack[-1]是什么，如果是0的话，就+1，并且可以加到上一个左括号的值
        上去，stack[-1]+=，相当于一个路径。如果上一个不为0，那就是(())这种了，就乘2
        一开始补一个0是为了让最后一步的时候，可以用stack[-1]继续加。否则就要单独判断一下
        """
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop()
                if v == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * v
        return sum(stack)

def scoreOfParentheses(S: str) -> int:
    """
    :param S:
    :return:
    每个左括号不是乘就是加，记录每个左括号的状态，栈是混合栈
    """
    s = S
    if s == '':
        return 0
    if s == '()':
        return 1
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append("(")
        else:
            if stack[-1] == "(":
                stack.pop()
                stack.append(1)
            else:
                tmp = 0
                while stack[-1] != "(":
                    tmp += stack.pop()
                stack.pop()
                stack.append(tmp * 2)
    return sum(stack)
if __name__ == '__main__':
    S = '(())'
    print(scoreOfParentheses(S))