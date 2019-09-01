#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def get_longgest_common(s1,s2):
    if s1 == '' or s2 == '':
        return 0
    ans = 0
    min_len = min(len(s1),len(s2))
    p = 0
    while p < min_len:
        if s1[p] == s2[p]:
            ans += 1
        p += 1
    return ans

if __name__ == '__main__':
    string_dict = {}
    n = int(input().strip())
    for i in range(n):
        string_dict[i+1] = input().strip()
    while True :
        s = input().strip()
        if s == "":
            break
        else:
            a, b = list(map(int,s.split(" ")))
            if a <= n and a >= 1 and b <= n and b >= 1:
                print(get_longgest_common(string_dict[a],string_dict[b]))