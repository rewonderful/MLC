#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def makesquare( nums):
    """
    算法：递归/DFS
        【事实上本方法在提交的时候TLE了，但是奇葩的是官方给出的solution就是这样的并且java版本的就能通过，
         所以很奇怪。主要记录思路吧！】
    思路：
            将列表内所有元素拼接起来能构成一个正方形。也就是说将所有元素按一定规则分配到4条边上，这4条边等长
        所以可以考虑设置4个bucket，对每个元素进行放入的测试。所有元素都放完且各条边的长度都等与sum/4的时候
        就说明有解否则无解。其实相当于将nums划分为4个互不相交的子集，且每个子集的sum都相等，等于sum/4
            直接递归所有可能很慢，所以要做一些剪枝操作：
            1. 如果 len(nums)<4，肯定构不成正方形，return False
            2. 如果sum(nums)%4 ！= 0，肯定构不成正方形，return False
            在dfs的过程中，用bucket记录元素累加的值，每次递归的时候是对元素进行递归，所以传递的是i，用nums[i]
        取元素，对4个桶的每个桶都进行测试放入，只有nums[i] + bucket[j] <= side时才放入并更新bucket。放入
        后对下一个元素进行递归，这里注意要根据下一层递归return的True False来定义当前层递归return的True和False
        如果下一层return的是False，用bucket[j] -= nums[i]剔除刚才对bucket[j]施加的影响，如果当前递归层整个for
        循环后都没有找到合适的放置位置，那就return False，说明没得放

        注意！
            这里要注意学习人家这种return 的方式，不一定非要在一开始的递归停止处才能将结果return回去，事实上这种
        return方式是从最后一层开始逐层将当前层的结果return回去，即下一层如果True，那我本层也返回True，如果下一层
        是False，并且所有的下一层递归都是False，那么我就返回False，相当于树里面，当前层是一个中间节点，我这个中间
        节点返回True 还是False取决于后续节点的return值，只要后面有一个True的我就True否则全是False我就也是False
        通过这种方式将结果带出来，不一定非要是前面做的那几种靠result列表带出的方式
    复杂度分析：
        时间：O4^N，因为我们总共有N根火柴棍对于每根火柴棍，我们有4个不同的它们可能属于的子集的可能性，或者它们可能
        是正方形的一部分。
        空间：ON,对于递归解决方案，空间复杂度是所有递归调用占用的堆栈空间。这里最深层的递归调用大小为N，因此空间复
        杂度为O(N)在这个解决方案中，除了递归堆栈之外，没有其他空间了
    """
    if len(nums) < 4 or sum(nums)%4 != 0:
        return False
    nums.sort(reverse=True)
    side = sum(nums)//4
    bucket = [0,0,0,0]
    def dfs(i,bucket):
        if i == len(nums):
            return bucket[0] == side and bucket[1] == side and bucket[2] == side and bucket[3] == side
        for j in range(4):
            if nums[i] + bucket[j] <= side:
                bucket[j] += nums[i]
                if dfs(i+1,bucket[:]):
                    return True
                bucket[j] -= nums[i]
        return False
    return dfs(0,bucket)

if __name__ == '__main__':
    print(makesquare([5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]))