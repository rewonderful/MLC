#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def scoreOfParentheses( S):
    """
    :type S: str
    :rtype: int
    """
    stack = []
    score = 0
    for char in S:
        if len(stack) == 0 :

        else:
            if char == "(":
               stack.append(char)
               score
            else:
                stack.pop()
if __name__ == '__main__':
    S = '(())'
    print(scoreOfParentheses(S))