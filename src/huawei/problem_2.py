#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import string
def solution(s):
    # # uppercase = string.ascii_uppercase
    # #     # print(uppercase)
    # #for i in
    #
    # s = s.lower()
    # s = s[::-1]
    # ans = ""
    # for char in s :
    #     if char == " ":
    #         ans += "0"
    #     else:
    #         ans += char
    # return ans
    ans = ''
    for char in s:

        if ord(char) >= 65 and  ord(char) <= 90:
            ans = chr(ord(char)+32) + ans
        elif char == " ":
            ans = "0" + ans
        else:
            ans = char + ans
    return ans





if __name__ == '__main__':
    s = input().strip()
    #s = "abcdefg"
    print(solution(s))
