#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import matplotlib.pyplot as plt


def lengthOfLIS_7( nums) :
    if nums == []:
        return 0
    ans = 1
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        ans = max(ans, dp[i])

    return ans
def lengthOfLIS( nums):
    """
    算法：动规
    思路：
            如果设立动规状态dp(i)为前i个元素组成的最长上升序列的长度的话，dp(i)和dp(i-1)建立不起来联系，
        因为这里的升上序列不要求是连续的，元素可以是跳着的
            设立动规状态dp(i)为以第i个元素为结尾的最长上升序列的长度，则dp(i)所代表的序列中，nums[i]是
        最大以nums[i]为结尾的最长上升序列中的最后一个元素
            显然，dp[i]初始化为1，亦即边界条件
            状态转移方程：
                dp(i)与dp(i-1)的关系是，如果nums[i] > nums[i-1]，显然dp(i) = dp(i-1) + 1
                但是如果不大于nums[i-1]的话，就应该在nums[0:i]之间找nums[j]<nums[i]的最大的那个dp(j)+1
                的值，dp(i) = dp(j_the_max)+1
                故用一个for 从(0:i)遍历并判断与更新
    复杂度分析：
        时间：ON2，两层for，且都和N相关
        空间：ON，dp列表的空间
    """
    if not nums:
        return 0
    dp = [1] * len(nums)
    ans = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
        ans = max(ans, dp[i])
    return ans

def lengthOfLIS1( nums):
    """
    算法：二分查找
    思路：
        维护一个数组stack,stack中记录的是，遍历到某个元素时，含当前元素的递增子序列
        用二分查找找到当前元素num的插入位置

            如果当前元素num比所有元素都大,即大于栈顶元素，那么push压栈
            否则说明在第i个位置处的元素stack[i]不大于num，用【二分查找】找到这个位置pos
            并另stack[pos] = nums[i]
            注意如过nums[i]和stack中的元素相等的话，比如stack = [1,2],nums[i] = 2
            二分查找得到的pos会等于2，超出数组长度，然而当元素相等的时候，其实是不用替换操作的，
            所以要用 stack[pos-1] != nums[i]来做限定
        最后len(stack)就是保存的最长递增序列的长度
        （因为递增子序列是有序的，所以这里用二分）
    复杂度分析：
        时间：NlogN，外面for循环ON，内部二分查找logN
        空间：OK，K为最长子序列长度
    """
    import bisect
    if not nums:
        return 0
    stack = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > stack[-1]:
            stack.append(nums[i])
        else:
            pos = bisect.bisect(stack, nums[i])
            if stack[pos - 1] != nums[i]:
                stack[pos] = nums[i]

    return len(stack)



if __name__ == '__main__':
    print(lengthOfLIS3([4,10,4,3,8,9]))
