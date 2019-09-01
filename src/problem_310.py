#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findMinHeightTrees7( n, edges):
    ans = []
    if n == 1:
        return [0]
    graph = [[] for _ in range(n)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    margin_node = [i for i in range(n) if len(graph[i]) == 1]
    while n > 2:
        new_margin_node = []
        n -= len(margin_node)
        for node in margin_node:
            neighbor = graph[node][0]
            graph[neighbor].remove(node)
            if len(graph[neighbor]) == 1:
                new_margin_node.append(neighbor)
        margin_node = new_margin_node
    return margin_node
def findMinHeightTrees(n, edges):
    """
    算法：类似于拓扑排序/剥洋葱
    思路：
        1.构建图
        2.将图中度为1，即叶子节点，即邻居数量只有1的节点构成叶子节点集合
        3.类似拓扑排序，循环剥离图中的叶子节点
        4.图中剩余的最后2个节点就是最小树的根节点
        分析：
            树的深度-->根节点到叶子节点的最大距离
            所以要想找到最小位置的根，它的位置应该在图中最长路径链的中间那一个或者两个，奇数长度就是1个，偶数长度就是两个
        为什么呢？
            注意上面提到的树的深度问题，若想把一个图转为最小高度的树，不论树是什么样的，图中的那条最长链总是要被分配到叶子
        节点中的对吧，而考察树的关键就是看根到最深的叶子节点的距离，那么显然，若要构建最小的树，就应该在最长路径中找根节点，
        将最长的两个叶子端点合理分配才可以达到最小高度的树。
            可以简单地想想证明一下为什么一定是在最长路径中。假设根节点P不在最长路径中，那么P到最路径AB中，还会走一段距离PO，
        则以P为根节点的树到达AB两端的距离是PO+PA和PO+PB，不论O在任何位置，一定有以下等式成立：
            max(PO+PA,PO+PB) > (AB)/2
                    p
                    .
             A......O....B
            那么如何分割一条直线使两子线段中的最长线段最小呢？max(l1,l2)，那自然是从中间划分，所以根在最长路径重点1个或2个位置
            所以题解中采用了"剥洋葱"式的解法，将最外层的叶子节点一点一点剥离，看似是在剥离所有叶节点，其实目的是为了将最长路径的两个端点
        同步的一点一点的剥离就像1,2,3,4,5,6,7,8,9 从1和9逐步向内侧剥离，左右指针以步长为1的速度同时向内侧走，最后剩下的中间的5就是
        中点。而因为树的深度取决于这个最长路径，所以其他节点的高度一定小于这个最长路径的两个端点在树中的深度，所以剥离过程中就一并剔掉
        了，剩余的就是根节点了！
    复杂度分析：
        时间：ON，for，while，都是ON
        空间：ON，graph的空间等
    -------------------------------------------------------------------------------------------------------------------------------------
    A).关于无向无环图找最长链任选一节点找终点再由终点找另一端点的证明：
    无向无环图所构成的最低高度树的根必为最长路径的中点或者两点，假设最长路径的端点为A,B
    Proof:
        1.若以路径上其他点为根，则该点到某一端会更长；
        2.若以不在路径AB上的点P为根，假设P到AB两个端点的路径与AB交点为O
    （注意只能有一个交点，否则会成环），则path(PO)+path(OA) or path(PO)+path(OB) 必有一个大于最长路径取中点的高度
         max(PO+PA,PO+PB) > (AB)/2
                            p
                            .
                            .
                        A…….O....B
    B).关于无向图求最长路径的方法，任选一个节点Q，dfs/bfs到最远点W停止，则QW为Q为起点的最长路径，W必为图最长路径的一个端点，再以此端
    点W起步dfs/bfs找到另一个端点M，则WM为图的最长路径
    proof:假设Q为起点的最长路径QW若不为图最长路径的端点：假设Q通过l1路径与图最长路径AB交于q,
    1.该路径不与图最长路径相交，不可能，因为若max(Aq,Bq)+qQ<QW,则可以构造新的最长路径max(Aq,Bq)+qQ+QW>Aq+Bq
                            Q
                            .
                            .
                        A…….q….B
                            .
                            W
    2.该路径QW与AB相交于q点，若该路径Qq+qW>Qq+max(qA,qB),可推出qW>max(qA,qB),可构造新最长路径max(qA,qB)+qW>qA+qB

    故该路径必为图最长路径的端点，证毕
    """
    if n == 1:
        return [0]
    graph = [[] for _ in range(n)]
    for begin, end in edges:
        graph[begin].append(end)
        graph[end].append(begin)
    leaves = [i for i in range(len(graph)) if len(graph[i]) == 1]

    while n > 2:
        newleaves = []
        n -= len(leaves)
        """
        一次剥一圈，这样的话如果最后的确剩下了两个，那么这俩就都留下来，如果用课程安排问题那样的拓扑排序的话
        一个一个的剥，最后肯定是能剥到根节点，但是只能留下1个结点
        """
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                newleaves.append(neighbor)
        leaves = newleaves
    return leaves

def findMinHeightTreesWrong(self, n, edges):
    """
    My Method  超时TLE了！！
    ⚠️⚠️求树的深度应该用层次遍历比较直观！深搜求深度不直观！⚠️⚠️️
    暴力地依次尝试每一个节点为根节点求深度，最小深度对应的就是解
    # 1.构建图，维护一个min_depth
    # 2.遍历图的每个节点，深搜到图的最大深度，即树的深度，最大深度小于=min_depth,则更新

    """
    graph = [[] for _ in range(n)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    result = []
    min_depth = float('inf')

    def dfs(i, depth, visit):
        visit[i] = 1
        record = [depth]
        for j in graph[i]:
            if visit[j] == 0:
                record.append(dfs(j, depth + 1, visit))
        return max(record)

    for i in range(n):
        depth = dfs(i, 0, [0] * n)
        if depth == min_depth:
            result.append(i)
        elif depth < min_depth:
            result.clear()
            min_depth = depth
            result.append(i)
    return result

if __name__ == '__main__':
    #print(findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
    print(findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
