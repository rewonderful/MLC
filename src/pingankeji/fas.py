#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json


def solution(graph):
    in_degree = dict()
    nodes = set()
    for k, v in graph.items():
        nodes.add(k)

        if k not in in_degree:
            in_degree[k] = 0
        for node in v:
            if node not in in_degree:
                nodes.add(node)
                in_degree[node] = 1
            else:
                in_degree[node] += 1
    queue = []
    for k, v in in_degree.items():
        if v == 0:
            queue.append(k)
    n = len(list(nodes))
    count = 0
    while queue:
        node = queue.pop(0)
        count += 1
        for k in graph[node]:
            in_degree[k] -= 1
            if in_degree[k] == 0:
                queue.append(k)
    if count == n:
        return "False"
    else:
        return "True"


if __name__ == '__main__':
    s = input()
    graph = json.loads(s)

    print(solution(graph))

