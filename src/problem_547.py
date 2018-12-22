#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    算法：并查集
    思路：
        本题有很强的并查集题目的特征，使用并查集数据结构可以比较直观地解题，先看并查集如何解题：
            遍历邻接矩阵M，如果M[i][j]==1即二者是朋友，那么合并i,j集合，遍历完整个矩阵M后则剩余
        的集合数量就是有多少个朋友圈
        --------------------------------------------------------------------------------
        并查集：
            直观来讲并查集就是将N个元素，同一类元素划分到一个集合中，集合是有标识的，对某个元素p的集合标识，
        就是id=set_id(p)
        并查集中主要的操作有两个，find和union，查找与合并
            查找find很好说，就是return set_id(p)
            合并union就是求集合的并，比如标识为id_P和id_Q的两个集合合并，就是将标识是id_P的所有元素，或者将
        id_P内的所有元素的标识id改成id_Q,这样原来id_P内的所有M个元素和id_Q内的所有N个元素合并，新的集合标识
        是id_Q(或者id_P),元素个数是M+N
            以列表元素构建并查集为例
                初始set_id=[i for i in range(n)]，每个元素的标识由下标来指定
                find(p) : return set_id[p]
                union(p,q):
                    如果find(p) == find(q)，那没啥事，return，也不用合并
                    否则，遍历整个set_id，将set_id = p的变成q，(或者q的变成p)
        以此构造是一种比较直观的线性表下的并查集，其复杂度为ON，因为要遍历所有set_id嘛
        --------------------------------------------------------------------------------
        基于线性的并查集，可以构建效率更高的并查集森林
            并查集森林将并查集节点构建成树状，合并和查找的效率更高，根节点作为set_id标识，如下图，元素2，1，0，3
        的并查集标识id就是2,元素4和5的set_id就是4，
        即find(2) = 2,find(1) = 2,...,find(4) = 4,find(5) = 5,二者Union后就是右边这样，整个树标识为2，这些元素同属
        一个并查集

                    2               4            2
                   / \             /            /| \
                  1   3   Union   5      -->   1 3  4
                 /                            /      \
                0                            0        5
"""
class DisjointSet:
    def __init__(self,n):
        self.set_id = [i for i in range(n)]
        self.set_size = [1 for _ in range(n)]
        self.count = n
    def find(self,p):
        while p !=self.set_id[p]:
            self.set_id[p] = self.set_id[self.set_id[p]]
            p = self.set_id[p]
        return p
    def union(self,p,q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.set_size[i] < self.set_size[j]:
            self.set_id[i] = j
            self.set_size[j] += self.set_size[i]
        else:
            self.set_id[j] = i
            self.set_size[i] += self.set_size[j]
        self.count -= 1
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        disjoint_set = DisjointSet(len(M))
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1 :
                    disjoint_set.union(i,j)
        return disjoint_set.count
def findCircleNum1(self, M):
    """
    算法：DFS
    思路：
        可以将题目转换为是在一个图中求连通子图的问题，给出的N*N的矩阵就是邻接矩阵，建立N个节点的visited数组，
        从not visited的节点开始深度优先遍历，遍历就是在邻接矩阵中去遍历，如果在第i个节点的邻接矩阵那一行中的第j
        个位置处M[i][j]==1 and not visited[j]，就应该dfs到这个第j个节点的位置，
    复杂度分析：
        时间：ON2?遍历所有节点
        空间：ON，visited数组
    """
    if M == [] or M[0] == []:
        return 0
    n = len(M)
    visited = [False] * n

    def dfs(i):
        visited[i] = True
        for j in range(n):
            if M[i][j] == 1 and not visited[j]:
                dfs(j)

    counter = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            counter += 1
    return counter

def findCircleNum2( M):
    """
    和上面相近，这里用BFS去遍历
    """
    if M == [] or M[0] == []:
        return 0
    n = len(M)
    visited = [False] * n

    counter = 0
    for i in range(n):
        if not visited[i]:
            queue = [i]
            while queue:
                index = queue.pop(0)
                visited[index] = True
                for j in range(n):
                    if M[index][j] == 1 and not visited[j]:
                        queue.append(j)
            counter += 1
    return counter
if __name__ == '__main__':
    print(findCircleNum1([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))