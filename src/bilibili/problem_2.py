# #!/usr/bin/env python
# # _*_ coding:utf-8 _*_

set_id = [i for i in range(100002)]
set_size = [1 for _ in range(100002)]
hash = [-1] * len(set_id)
def find( p):
    while p != set_id[p]:
        set_id[p] = set_id[set_id[p]]
        p = set_id[p]
    return p
def union( p, q):
    i = find(p)
    j = find(q)
    if i == j:
        return
    if set_size[i] < set_size[j]:
        set_id[i] = j
        set_size[j] += set_size[i]
    else:
        set_id[j] = i
        set_size[i] += set_size[j]
def solution():
    tmp = 0
    ans = 0
    for i in range(len(set_id)):
        x = find(i)
        hash[x] += 1
        if tmp < hash[x]:
            tmp = hash[x]
            ans = x
    return ans
if __name__ == '__main__':
    N = int(input().strip())

    for _ in range(N):
        x,y = list(map(int,input().strip().split(" ")))
        union(x,y)

    print(solution())



