#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def solution(s):
    ans = 0
    count = 0
    for char in s:
        if char == "[":
            count += 1
        else:
            count -= 1
        if count == -1:
            ans += 1
            count = 0

    return ans + count



if __name__ == '__main__':
    s = input().strip()
    print(solution(s))
