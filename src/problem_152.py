#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxProduct(self, nums):
    """
    Disscusion Method
        可以根据My Method 的动规的做法来引申出这种做法，动规是将每一刻的值都记录了下来，但是事实上
    都是遍历一次后，在某次遍历中给max_product赋最终结果值，所以就可以不用dp数组，相当于是O1的空间复杂度
    在遍历的时候，每一刻都记录当前的curr_min和当前的curr_max，然后在每一个位置都更新curr_min,curr_max，
    其实动规里也是这样做的，只不过动规中把结果存了下来，这里只用几个变量来存储，因为其实这种题对结果不要求存储
    的，最后只要能有一个变量返回值就oK了
        然后就是注意遍历的时候从下标1开始
        以及在计算的时候，curr_min会更新，而底下的curr_max还要用curr_min的值，所以要用tmp保存起来
        或者用one line code
        curr_min,curr_max = min(num, num*curr_min, num*curr_max),max(num, num*curr_min, num*curr_max)
        这样在计算curr_min,curr_max的算式中用的curr_min和curr_max就都是上一时刻的了
    """
    curr_min = nums[0]
    curr_max = nums[0]
    max_product = nums[0]
    for num in nums[1:]:
        min_tmp = curr_min
        curr_min = min(num, num * curr_min, num * curr_max)
        curr_max = max(num, num * min_tmp, num * curr_max)
        max_product = max(max_product, curr_max)
    return max_product
def maxProduct1(self, nums):
    """
    My Method
    算法：动规
    思路：
        首先是用动规做
        题目要求的是数组内连续元素的成绩，但是就像见过的若干题一样，连续数组不代表一定是从0到i的，
        所以设计动规的状态dp[i]表示以i结尾的情况
        一开始我只在dp[i]里存了最大的正数和，就像最大子序列的和一样，但是这样是欠妥的，考虑下面这个case
        [-3,2,-4],
        很明显最大子序列和是-3 * 2 * -4 = 24
        如果只用dp[i]存以第i个位置结尾的元素的最大正乘积的话，dp内会变成[0,2,0]，然后认为max_product = 2
        事实上由于元素可正可负，而负负得正，那么前面的元素成绩是负是允许的，并且可能会产生最优解
        所以我这里用dp[i]存以i结尾的最大的子序列乘积和最小的负最小子序列乘积
        dp[i] = [maxProduct,-minProduct]
        这样在遍历的时候，根据nums[i] >0,==0,<0可以分成三种
         nums[i] == 0 的时候显然maxProduct 和 -minProduct 都是0
         当nuns[i] >0时
            nums[i][0] = max(nums[i], nums[i] * dp[i - 1][0])
            nums[i][1] = nums[i] * dp[i - 1][1]   正负得正嘛
         反之亦然
         要注意这里的dp[i]虽然记录了两个值，正最大和负最小，真正要求的值还是dp[i][0]，所以要更新max_product

    """
    if nums == []:
        return 0
    dp = [[0, 0] for _ in range(len(nums))]
    dp[0] = [nums[0], 0] if nums[0] >= 0 else [0, nums[0]]
    max_product = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > 0:
            dp[i][0] = max(nums[i], nums[i] * dp[i - 1][0])
            dp[i][1] = nums[i] * dp[i - 1][1]
        elif nums[i] == 0:
            dp[i] = [0, 0]
        else:
            dp[i][0] = nums[i] * dp[i - 1][1]
            dp[i][1] = min(nums[i], nums[i] * dp[i - 1][0])
        max_product = max(max_product, dp[i][0])
    return max_product


if __name__ == '__main__':
    print(maxProduct([-2,0,-1]))