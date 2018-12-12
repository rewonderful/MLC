#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def canConstruct( ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True
if __name__ == '__main__':
    print(canConstruct("aa","aab"))