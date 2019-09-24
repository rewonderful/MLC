#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solution(words, M):
    ans =[]
    curr = []
    curr_len = 0
    for word in words:
        if curr_len + len(curr) + len(word) > M:
            for i in range(M - curr_len):
            #     if len(curr) == 1:
            #         curr[i] += ' '
            #     else:
            #         curr[i % (len(curr) - 1)] += ' '

                curr[i % (len(curr) - 1 or 1)] += ' '
            ans.append(''.join(curr))
            curr = []
            curr_len = 0
        curr.append(word)
        curr_len += len(word)

    tmp = ' '.join(curr)
    for _ in range(M - len(tmp)):
        tmp += ' '
    ans.append(tmp)
    return ans


if __name__ == '__main__':
    # M = int(input().strip())
    # words = list(map(str,input().strip().split(" ")))
    M = 13
    words = list(map(str,"I have a dream Martin Luther King".strip().split(" ")))
    ans = solution(words,M)
    for string in ans :
        print(string)

