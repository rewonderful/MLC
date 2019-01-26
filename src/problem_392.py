#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    i = 0
    if (len(s) == 0):
        return True
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
        elif i == len(s):
            return True
    return i == len(s)