#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findOrder(self, numCourses, prerequisites):
    """
    My  Method Optimize
    算法：拓扑排序
    思路：
        相较于My  Method Basic
        最重要的改变就是用空间换时间，加了一个outdegree数组来记录每个节点的出度情况！这样也更直观！
        然后[x,y]的pair对在图的节点中是y-->neigbors (x)，把x记录在y的neighbor中，这样y 在队列
        中pop出去的时候，直接遍历y的neighbors就可以了，不用去遍历所有的节点，
        用outdegree出度数组来记录每个节点的出度，将出度为0的节点入队列
    复杂度分析：
        时间：ON，遍历一遍所有节点
        空间：ON，outqueue，graph，queue的存储空间

    """
    graph = [[] for _ in range(numCourses)]
    outdegree = [0] * numCourses
    for x, y in prerequisites:
        outdegree[x] += 1
        graph[y].append(x)
    queue = []
    for i in range(numCourses):
        if outdegree[i] == 0:
            queue.append(i)
    result = []
    while queue:
        node = queue.pop(0)
        numCourses -= 1
        result.append(node)
        for i in graph[node]:
            outdegree[i] -= 1
            if outdegree[i] == 0:
                queue.append(i)
    return result if numCourses == 0 else []
def findOrder1(self, numCourses, prerequisites):
    """
    My  Method Basic
    算法：拓扑排序
    思路：
        就是拓扑排序的思想
        要注意的是题目中的prerequisites的序列对[x,y]是x-->y，所以构建图的时候注意
        这种解法只击败3%的人，是比较愚钝的一种方法
        即只建立图的关系，然后图中节点的neighbor存储的是上面的x出发，x的邻居包含y

        👆这样解的话劣势就是，一个出度为0的节点pop后，必须遍历所有的其他图的节点才能将
        包含node的节点中的node remove掉，虽然我这里换成了集合set来加快查找，但是这样还是
        比较慢的！
    """
    graph = [set() for _ in range(numCourses)]
    for x, y in prerequisites:
        graph[x].add(y)
    queue = []
    for i in range(len(graph)):
        if len(graph[i]) == 0:
            queue.append(i)
    result = []
    while queue:
        node = queue.pop(0)
        numCourses -= 1
        result.append(node)
        for i in range(len(graph)):
            if i != node and node in graph[i]:
                graph[i].remove(node)
                if len(graph[i]) == 0:
                    queue.append(i)
    if numCourses != 0:
        return []
    else:
        return result
if __name__ == '__main__':
    print(findOrder(2,[[1,0]]))
