#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json


def solution(graph):

    visit = dict()
    for k, v in graph.items():
        visit[k] = 0
        for node in v:
            visit[node] = 0


    #visit = dict()

    def dfs(key):
        if visit[key] == -1:
            return False
        if visit[key] == 1:
            return True
        visit[key] = -1
        for node in graph[key]:
            if not dfs(node):
                return False
        visit[key] = 1
        return True

    for key in visit.keys():
        if visit[key] == 0 and not dfs(key):
            return False
    return True

if __name__ == '__main__':
    s = input()
    graph = json.loads(s)
    print(solution(graph))

