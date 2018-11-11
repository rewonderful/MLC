#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def longestPalindrome( s):
    longest = ''
    s_len = len(s)
    if s_len ==0 or s_len ==1:
        return s
    else:
        for i in range(len(s)):
            char = s[i]
            char_others = s[i+1:]
            if char not in char_others:
                continue
            else:
                for j in range(1,len(char_others)+1):
                    str = char +char_others[:j]
                    flag = False
                    str_length = len(str)
                    j_range = str_length/2 if str_length % 2 ==0 else (str_length-1)/2
                    for k in range(int(j_range)):
                        if str[k] != str[str_length-1-k]:
                            flag = False
                            break
                        else:
                            flag = True
                    if flag:
                        longest = str if len(str)>len(longest) else longest
    return longest if len(longest) > 1 else s[0]


    return
if __name__ == '__main__':
    s='abcccb'
    print(longestPalindrome(s))