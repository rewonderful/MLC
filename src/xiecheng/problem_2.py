#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def solution(s):

    ans = []
    str_ans = []
    i,j = 0,0
    visited = set()
    while j < len(s):
        if j == i and s[j] not in visited:
            visited.add(s[j])
            j += 1
        elif s[j] in visited :
            j += 1
        else:
            if j-i <=1:
                visited.add(s[j])
                j+= 1
            else:
                ans.append(j-i)
                str_ans.append(s[i:j])
                i = j
                visited = set()
                #j += 1
    if j != i:
        ans.append(j-i)
        str_ans.append(s[i:j])
    print(str_ans)
    return ' '.join(map(str,ans))



    pass
if __name__ == '__main__':
    #s = input().strip()
    s = " aaaaddddffffeeadadad"
    print(solution(s))
