#!/usr/bin/env python
# _*_ coding:utf-8 _*_
n,m = map(int,input().split(" "))
in_node = []
edge_node = []
for _ in range(n):
    a1 = list(map(int,input().split(" ")))
    in_node += a1[1:-1]
    edge_node.append(a1[0])
    edge_node.append(a1[-1])
for j in range(m):
    a2 = list(map(int,input().split(" ")))
    if j == 0 or j == m-1:
        edge_node += a2
    else:
        in_node += a2
mul = n * m
in_node = sorted(in_node)
print(sum(in_node[:mul - 1]) + min(edge_node))