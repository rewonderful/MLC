#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#leetcode3
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def lengthOfLongestSubstring(s):
    max_len = 0
    begin = i = 0
    position = {}
    while i < len(s):
        curr = s[i]
        if curr in position and position[curr] >= begin:
            begin = position[curr] + 1
            position[curr] = i
        else:
            position[curr] = i
        max_len = max(max_len, i - begin + 1)
        i += 1
    return max_len



if __name__ == '__main__':
    #print(lengthOfLongestSubstring("bbbbb"))
    #s = input().strip()
    print(lengthOfLongestSubstring(input().strip()))




