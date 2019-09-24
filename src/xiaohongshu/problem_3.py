#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# def solution(N,B,S,p,v):
#     ans = (0,0,0)
#     dp = [[0] * (B + 1) for _ in range(N + 1)]
#     for i in range(1,N+1):
#         for j in range(1,B+1): #dangqian yusuan
#             dp[i][j] = dp[i-1][j]
#             if j >= p[i-1] :
#                 dp[i][j] = max(dp[i][j], dp[i-1][j-p[i-1]]+v[i-1])
#             # if dp[i][j] > ans[0]:
#             #     ans = (dp[i][j],,i)
#
#
#     return dp[-1][-1]




if __name__ == '__main__':
    #     # N,B,S = list(map(int,input().strip().split(' ')))
    #
    #
    #     # p,v = [],[]
    #     # for _ in range(N):
    #     #     pi,vi = list(map(int,input().strip().split(' ')))
    #     #     p.append(pi)
    #     #     v.append(vi)



    ans = (0, 0, 0)
    def dfs(remain,yusuan,left_count):
        global  ans
        if len(remain) == 0 or left_count == 0:
            return
        for i in range(len(remain)):
            p, v = remain[i]
            if yusuan >= p and left_count >= 1:
                if v + ans[0] > ans[0]:
                    ans = (ans[0]+v,ans[1]+p,S-left_count+1)
                elif v + ans[0] == ans[0]:
                    if ans[1] + p < ans[1]:
                        ans = (ans[0] + v, ans[1] + p, S - left_count+1)
                    elif ans[1] + p == ans[1]:
                        if S - left_count < ans[2]:
                            ans = (ans[0] + v, ans[1] + p, S - left_count+1)

                dfs(remain[i:],yusuan-p,left_count - 1)
            else:
                dfs(remain[i:], yusuan, left_count, )

    items = [(1, 100), (5, 200), (11, 300)]
    # p = [1,5,11]
    # v = [100,200,300]
    N, B, S = 3, 10, 1

    dfs(items,B,S)
    print(ans)



