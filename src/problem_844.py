#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    stack_S = []
    for s in S:
        if s == '#' :
            if stack_S:
                stack_S.pop()
            else:
                continue
        else:
            stack_S.append(s)
    stack_T = []
    for t in T:
        if t == '#' :
            if stack_T:
                stack_T.pop()
            else:
                continue
        else:
            stack_T.append(t)

    return stack_S == stack_T
if __name__ == '__main__':
    # S = 'ab#c'
    # T = 'ad#c'
    S = "y#fo##f"
    T = "y#f#o##f"
    print(backspaceCompare(S,T))