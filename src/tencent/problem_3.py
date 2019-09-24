#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def solution(self,x,y,n,k):


        self.ans = 0
        def dfs(i,count,total,difficulty):
            if count == k or i >= n:
                return
            dfs(i+1,count,total,difficulty)
            dfs(i + 1,count + 1,total+x[i],min(difficulty,y[i]))
            self.ans = max(self.ans, (total+x[i]) * min(difficulty,y[i]))

        dfs(0,0,0,float("inf"))
        return self.ans


if __name__ == '__main__':
    n, k = list(map(int,input().strip().split()))
    x = []
    y = []
    for _ in range(n):
        xi,yi = list(map(int,input().strip().split()))
        x.append(xi)
        y.append(yi)
    solution = Solution()
    print(solution.solution(x,y,n,k))