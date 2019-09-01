#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def canFinish7( numCourses, prerequisites):
    if numCourses == 0:
        return True
    in_degree = [[] for _ in range(numCourses)]

    out_degree = [0] * numCourses

    for x, y in prerequisites:
        # x-->y
        out_degree[x] += 1
        in_degree[y].append(x)
    zero_queue = []
    for i in range(numCourses):
        if out_degree[i] == 0:
            zero_queue.append(i)
    while len(zero_queue) > 0:
        course = zero_queue.pop(0)
        numCourses -= 1
        for other_course in in_degree[course]:
            out_degree[other_course] -= 1
            if out_degree[other_course] == 0:
                zero_queue.append(other_course)
    return numCourses == 0
def canFinish( numCourses, prerequisites):
    """
    算法：深搜
    思路：
        题中很明显地提示了这是一个图的结构
        对图进行遍历，如果图中有环则一定不能完成，否则可以完成
        因此将本题转化为判断给定的图中是否含环的问题

        深搜遍历图的话，如何判断有环？
            在遍历过程中，如果从某节点出发深度遍历，某时刻又遍历回本节点，则说明图中有环！
        因此：
            1. 首先构建图的深度优先遍历的整体框架，构建图的结构
            2. 构建visitied列表记录节点是否被访问
            3. 设定节点三个状态
                0：未被访问
                -1：正在被访问，即正在从该节点出发向下递归深度遍历
                1：该节点已被访问过
            4. 从某节点开始深度遍历，遍历时先置该节点状态为-1，如果后序节点中都没有重复访问本节点
               的visit状态，说明没有环，才可以将该节点visit置1，visit[i]=1
               所以递归函数的一开始要先判断当前节点的状态是否为-1,即visit[i] == -1，如果为-1则应该
               返回False，说明当前正在访问的节点已经是上一层中正在访问的节点了！

    注意：
        1. 在递归的过程中，如果visit[i]==1说明已经访问过了，注意，这里的已经访问过和存在环的重复访问
           的已经访问过不同！如果==1说明肯定是没问题的访问，直接return True就好，它对应的情况是指那种
           因为main函数外面的for循环导致先访问的节点会置True，后面再访问时已经True了，比如样例：
            2，[[0,1]],图结构:1-->0，由于外面的for循环，会先访问节点0，然后置visit[0]=1，而后面
            从1开始访问到0的时候，就已经知道0的visit状态是1就直接返回Ture就好，事实上如果还是有点混淆
            的话，不写这句也可以，写上只是加快运行罢了
                    if visit[node.val] == 1:
                        return True
        2. 注意这种递归的返回方式，要将底层的递归bool结果返回，可以在if中判断，根据if的结果在return False
         or True
        3. 注意dfs中的循环里的条件，不用判断visit[neightbor] ==0，否则的话将无法到达有环的那个节点！
        因为有环的话，下一个节点的状态可能就是-1，如果只判断==0才往下递归，那永远return的是True！
        所以就直接向下递归就好了，如果有环就判断是-1，return False，正常的话，就正常的返回True并且将后面
        的节点的vist状态置1

    复杂度分析：
        时间：ON,遍历所有节点
        空间：ON，递归栈空间，辅助建立图，以及visit的空间
    """
    visit = [0] * numCourses

    class GraphNode:
        def __init__(self, x):
            self.val = x
            self.neighbors = []

    graph = [GraphNode(i) for i in range(numCourses)]

    for pair in prerequisites:
        graph[pair[1]].neighbors.append(graph[pair[0]])

    def dfs(node):
        if visit[node.val] == -1:
            return False
        if visit[node.val] == 1:
            return True
        visit[node.val] = -1
        for neighbor in node.neighbors:
            if not dfs(neighbor):
                return False
        visit[node.val] = 1
        return True

    for node in graph:
        node_notvisited = visit[node.val] == 0
        if node_notvisited and not dfs(node):
            return False
    return True

def canFinish1( numCourses, prerequisites):
    """
        实际上上面的代码是参照这个代码构建出来的，上面代码是用本解法在我的思路和数据结构的模式下构建出来的
        这里的解法对图的结构进行了简化，即用二维列表带代表图的结构，下标代表图的val,graph[i]对应图中的一个
        节点，每个节点都是一个列表，和我上面自己写的GraphNode是相同的作用，但是这样写更简化
    """
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]
    for x, y in prerequisites:
        graph[y].append(x)

    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True

    for i in range(numCourses):
        if visit[i] == 0 and not dfs(i):
            return False
    return True

def canFinish2(numCourses, prerequisites):
    """
    算法：拓扑排序/宽度优先搜索
    思路：
        拓扑排序在判断DAG有向无环图中，本来就是可以检测图中是否有环存在的一种方法，其思想如下：
            1. 构建一个图，计算好所有节点的入度
            2. 将入度为0的节点依次从图中拆解下来，拆解入度为0的节点时同时拆解掉以他为起始点的边
            3. 更新剩余节点的入度，选择入度为0的点回到第2步继续上述过程，直到整个图中没有入度为0的点为止
            如果都拆完后所有节点都拆掉了，即没有剩余节点，则这个图内无环，否则有环
        所以对比此题：
            1. 构件图，用列表记录所有节点的入度
            2. 建立一个队列queue记录入度为0的节点
            3. 拆解入度为0的节点-->从queue中弹出节点
                 将弹出节点的neighbors的入度 -= 1 （拆解边）
                 若-=1后入度为0则入队列
                 记录队列中弹出元素的counter += 1
            4. 判断counter是否等于原节点数，若相等，则无环，否则有环
    复杂度分析：
        时间：ON，遍历所有节点
        空间：ON，构建图，入度列表什么的空间
    """
    graph = [[] for i in range(numCourses)]
    indegree = [0] * numCourses
    for x, y in prerequisites:
        indegree[x] += 1
        graph[y].append(x)
    queue = []
    k = 0
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.pop(0)
        k += 1
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    return k == numCourses


def canFinish3(numCourses, prerequisites):
    """
    My Method --> 拓扑排序
    和上面的canFinish2一样的思路，只不过用了我的数据结构GraphNode
    """
    class GraphNode:
        def __init__(self, x):
            self.val = x
            self.neighbors = []

    graph = [GraphNode(i) for i in range(numCourses)]
    indegrees = [0] * numCourses
    for end, begin in prerequisites:
        indegrees[end] += 1
        graph[begin].neighbors.append(graph[end])
    queue = []
    for i in range(len(indegrees)):
        if indegrees[i] == 0:
            queue.append(i)
    count = 0
    while queue:
        node_index = queue.pop(0)
        node = graph[node_index]
        count += 1
        for neighbor in node.neighbors:
            indegrees[neighbor.val] -= 1
            if indegrees[neighbor.val] == 0:
                queue.append(neighbor.val)
    return count == numCourses
if __name__ == '__main__':
    print(canFinish3(2,[[0,1]]))