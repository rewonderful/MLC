#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def isValid( s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 != 0:
        return False
    match = {'(': ')', '{': "}", "[": ']', ')': '(', ']': '[', '}': '{'}
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            if char in match and match[stack[-1]] == char:
                stack.pop()
                continue
            else:
                stack.append(char)
    return not stack #最后栈为空的话说明是匹配有效的，栈非空的话说明是无效的
if __name__ == '__main__':
    s = "[({{()}})]"
    print(isValid(s))