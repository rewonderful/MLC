def updateMatrix( matrix):
    """
    Sulotion DP Method
    算法：动规
    思路：
        一般的动规是从某个确切的地方出发， 比如一般的二维矩阵的题可能就是从左上角出发去右下角比较直观，
        但是本题并没有这个限制，所以事实上可以从任何一个位置出发，但是不妨就选定从左上出发到右下，因为
        这样的话也一定可以将整个二维矩阵都访问，但是要注意的是，这里仅从坐上到右下一遍是不够的！还需要
        右下到坐上再来一遍！
        ⚠️⚠️⚠️💥🌟⚡️🌟：
            因为一般的递归，是不会产生死循环的，比如从左上到右下的过程中，下一时刻的状态和前一时刻的
        状态一定是分割开来的，但是本题事实上是上下左右四个方向，所以如果一次遍历将四个方向都访问的话
        一定会造成死循环,如下图所示，会有循环依赖的问题！所以要两遍不存在循环依赖的遍历，先左上再右下
            ------------
            | a→|←b→|←c |
            --↓↑--↓↑--↓↑-
            | d→|←e→|←f |
            --↓↑--↓↑--↓↑-
            | g→|←h→|←i |
            -------------
    复杂度分析：
        时间：ORC*2，R是行数，c是列数，其实就是ON2了
        空间：ORC*2，dp数组空间
    """
    if matrix == []:
        return []
    m, n = len(matrix), len(matrix[0])
    dp = [[float('inf')] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == 0:
                dp[i][j] = 0
            else:
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
    return dp

def updateMatrix1( matrix):
    """
    Sulotion Method
    算法:BFS宽度优先遍历
    思路：
        本思路是基于暴力解法来的改进版，所以先看一下暴力解法的思路：
            遍历矩阵，如果matrix[i][j] == 0 的话，ans[i][j]=0,否则matrix[i][j] == 1时从这个1的位置出发
        遍历附近所有的节点，找到最近的0，距离是abs(r-i)+abs(c-i)，非常暴力，耗时，并且这样的思路是基于
        ⚠️ ⚠️【一次遍历只更新一个matrix[i][j] == 1位置的ans[i][j]的值】
        所以改进的方法就是，从matrix[i][j] == 0出发，一次更新所有matrix，0附近的所有ans大于它的那些位置的值
        这样一次可以更新多点
            并且要使用BFS来保障一次更新周围紧邻的所有位置，BFS又需要queue，所以这里设置queue来辅助
        注意️💥⚡️🌟：
            BFS的特性是从某点出发，BFS第一次碰到该点的时候一定是经过了最短的搜索步数，可以拿二叉树的层次遍历
        来类比理解。所以从1到0的最短间隔，反过来，也是这个0到这个1的最短间隔，所以从0出发BFS来简化问题

        故：
            1.先遍历一次，然后将所有matrix[i][j] == 0的位置入队列并且设ans[i][j] = 0
            2.对队列中每个位置i，j的四个方向的紧邻位置r,c进行更新，
                位置合法且ans[r][c] > ans[i][j] + 1
                则更新ans[r][c] = ans[i][j] + 1
                并且将r,c入队列，因为刚才只是把所有0入队列了，被更新的新的位置往往都是1，而只遍历所有0的紧邻
                节点可能是无法到达下面的1的，所以这里要把r,c入队列，并且这里的queue本来就是为了BFS，BFS可以
                得到最近的解，也就应该这样逐级入队列
    复杂度分析：
        时间：ORC，
        空间：ORC，ans空间
    """
    if matrix == []:
        return []
    ans = [[float('inf')]*len(matrix[0]) for _ in range(len(matrix))]
    queue = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                ans[i][j] = 0
                queue.append((i, j))
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        i, j = queue.pop(0)
        for i_delta, j_delta in direction:
            r = i + i_delta
            c = j + j_delta
            if r >= 0 and r <= len(matrix) - 1 and c >= 0 and c <= len(matrix[0]) - 1 and ans[r][c] > ans[i][j] + 1:
                ans[r][c] = ans[i][j] + 1
                queue.append((r, c))
    return ans
if __name__ == '__main__':
    print(updateMatrix1([[0,0,0],[0,1,0],[1,1,1]]))






