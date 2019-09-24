#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def solutoin(n,graph):
    visited = set()
    ans = []
    out_degree = [-1]*(n + 1)
    queue = []
    in_graph = [[] for _ in range(n + 1)]
    for i in range(1,n+1):
        for j in graph[i]:
            in_graph[j].append(i)

    for i in range(1,n+1):
        out_degree[i] = len(graph[i])


    for i in range(1,n+1):
        if i in visited:
            ans.append("0")
        else:
            count = 0
            queue = []
            for j in range(1, n + 1):
                if out_degree[j] == 0 and j != i:
                    queue.append(j)
            while queue:
                node = queue.pop(0)
                visited.add(node)
                count += 1
                for j in in_graph[node]:
                    out_degree[j] -=1
                    if out_degree == 0:
                        queue.append(j)
            ans.append(str(count))

    return " ".join(ans)





if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i] = list(map(int,input().split(" ")))[1:]


    print(solutoin(n,graph))