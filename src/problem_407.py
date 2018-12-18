#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def trapRainWater(self, heightMap):
    """
    Disscusion & XiaoXiang Method
    算法：BFS+heqp
    思路：
            首先要明确，一个位置能盛多少水，取决于该位置上下左右4个位置的height大小，并且仅取决与最短的那一块，类似于最短木板理论
        将围起来的部分视为墙，整个矩阵一定是最外面一圈是最基本的墙，因为最外面的一圈一定不盛水，所以取最外面的一圈作为初始的墙

        因为最短木板理论，以最矮的墙开始去找盛水点，从最矮位置i,j出发
            因为对整个矩阵而言，整个最外侧的一层墙会决定整个矩阵的盛水多少，所以将最外层的墙建立最小堆进行遍历，并且可以想象
            成是以最外层的墙的高度有小到大，视为整个容器被水面包着，水面从1升到2，再升到3这样
            并且哪怕墙内的某个点r,c处，其上下左右位置，其他三个位置都很高，这无所谓，因为r,c的盛水量取决于最短模板，而最短
            的那部分就是当前的最矮位置i,j，所以从最矮位置i,j出发到达r,c时，即i,j是r,c上下左右邻居中的一个，对r,c而言，i,j
            因为是当前最外层墙中最小的，max(0,height[i][j]-height[r][c])一定是r,c位置处的盛水量，r,c位置的盛水量已知，且
            后序不会变，因为当前计算r,c的盛水量时已经是它所在情况下的最小板形成的盛水量了，并且在遍历过r,c后，r,c就变成
            它邻居的新的墙，add到堆，并且高度是当前max(max(heightMap[r][c], height[i][j])，并且为了避免遍历中产生环，设
            立visited数组记录访问情况
        ------------------------------------------------------------------------------------------------------------
    Disscusion Thought：
        注意几个理论
            1. 从matrix四周开始考虑，发现matrix能Hold住的水，取决于height低的block
            2. 必须从外围开始考虑，因为水是被包裹在里面，外面至少需要现有一层
            以上两点就促使我们用min-heap: 也就是natural order的PriorityQueue<Cell>.
        Steps
            1. process的时候，画个图也可以搞清楚: 就是四个方向都走走，用curr cell的高度减去周围cell的高度.
            2. 若大于零，那么周围的cell就有积水: 因为cell已经是外围最低, 所以内部更低的, 一定有积水.
            3. 每个visited的cell都要mark, avoid revisit
            4. 根据4个方向的走位 `(mX, mY)` 创建新cell 加进queue里面: cell(mX, mY) 已经计算过积水后, 外围墙小时, `(mX, mY)`就会变成墙.
            5. 因为做的是缩小一圈的新围墙, height = Math.max(cell.h, neighbor.h);
            和trapping water I 想法一样。刚刚从外围，只是能加到跟外围cell高度一致的水平面。往里面，很可能cell高度变化。
            这里要附上curr cell 和 move-to cell的最大高度。
        为什么想到用Heap (min-heap - priorityQueue)
            要找到bucket的最短板
            每次需要最先处理最短的那条 (on top)
        为什么从外向里遍历：
            木桶理论, 包水, 是从外面包住里面
            洋葱剥皮, 用完丢掉
    复杂度分析：
        时间：ON2?
        空间：ON2，visited空间，队列空间
    """
    if not heightMap or not heightMap[0]:
        return 0
    import heapq
    m = len(heightMap)
    n = len(heightMap[0])
    visited = [[False] * n for _ in range(m)]
    result = 0
    priority_q = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                heapq.heappush(priority_q, (heightMap[i][j], i, j))
                visited[i][j] = True
    while priority_q:
        height, i, j = heapq.heappop(priority_q)
        for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if r >= 0 and r <= m - 1 and c >= 0 and c <= n - 1 and not visited[r][c]:
                result += max(0, height - heightMap[r][c])
                visited[r][c] = True
                heapq.heappush(priority_q, (max(heightMap[r][c], height), r, c))
    return result