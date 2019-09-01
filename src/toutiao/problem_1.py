#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solution(matrix,N):
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 3:
                graph[i].append(j)
                graph[j].append(i)
    def dfs(i,visited):
        if not visited[i]:
            visited[i] = True
            for j in graph[i]  :
                if  not visited[j]:
                    dfs(j,visited)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if not visited[i]:
            dfs(i,visited)
            ans += 1
    return ans



if __name__ == '__main__':
    N = int(input().strip())
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input().strip().split(' '))))
    # graph = [[0,4,0],
    #          [4,0,0],
    #          [0,0,0]]
    print(solution(graph,N))