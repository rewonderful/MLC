#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# def solution(doors,balls):
#     line = [0]*1001
#     for a,b in doors:
#         for i in range(a,b+1):
#             line[i] = 1
#     ans = 0
#     for i in balls:
#         ans += line[i]
#     return ans
def solution(doors,balls):
    doors.sort(key=lambda x:x[0])
    new_doors = []
    for a,b in doors:
        if new_doors == []:
            new_doors.append([a,b])
            continue
        tail_start,tail_end = new_doors[-1]
        if a > tail_end:
            new_doors.append([a,b])
            continue
        elif a == tail_end or a >= tail_start and b >= tail_end:
            new_doors[-1][1] = b
    ans = 0
    for i in balls:
        for a,b in new_doors:
            if i >= a and i <= b:
                ans += 1
    return ans






if __name__ == '__main__':
    n,m = list(map(int,input().strip().split(" ")))
    doors = []
    for _ in range(n):
        tmp = tuple(map(int,input().strip().split(" ")))
        doors.append(tmp)
    balls = []
    for _ in range(m):
        balls.append(int(input().strip()))
    # doors = [(3,3),(1,5),(2,6),(7,8)]
    # balls = [2,4,8]


    print(solution(doors,balls))