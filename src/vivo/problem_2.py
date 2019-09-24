#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def solution(n,m):
    count = n

    ans = []
    visited = [0] * n
    k = 0
    while count != 0:
        i = k
        j = 1
        find_next = False
        has_circle = False
        while not find_next:
            if visited[i] == 1:
                i += 1
                if i == n:
                    i = 0
                    has_circle = True
                    continue
            else:
                if not has_circle:
                    j += 1
                i += 1
                if i == n:
                    i = 0
            if j % m == 0:
                find_next = True
        k = i
        ans.append(i + 1)
        visited[i] = 1
        count -= 1

    return ans

if __name__ == '__main__':
    print(solution(6,3))


