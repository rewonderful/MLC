#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findKthLargest( nums, k):
    """

    快排的思想
    根据pivot将左右两侧划分，在划分后就可以得到p，将p和k比较，如果k在p的左侧，那么就丢弃右侧，只排序左侧，如果k在右侧，那么就
    丢弃左侧，只排序右侧，
        要注意这里的partition一次排序是从大到小排
        注意第k大，所以要 p+1
        注意find_kth中的while是l<=r，有等于号
    复杂度：On
    """
    def partition(nums, l, r):
        pivot = nums[l]
        while l < r:
            while l < r and nums[r] <= pivot:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] > pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l

    def find_kth(nums, l, r):
        while l <= r:
            p = partition(nums, l, r)
            if p + 1 == k:
                return nums[p]
            elif k < p + 1:
                r = p - 1
            else:
                l = p + 1

    return find_kth(nums, 0, len(nums) - 1)

def findKthLargest(self, nums, k):
    import heapq
    """
    算法：前N大堆
        利用最小堆实现一个堆序列，其长度为k个元素，这k个元素组成的最小堆堆顶即是第K大的数字
        1. 首先初始化一个堆，python中用list，
        2. 从原数组nums中逐个将元素push到堆中，若堆的长度小于k时，当前元素直接插入即可
           当堆内元素已达k个时，要想push当前元素，就必须要求当前元素是大于当前堆顶(list中即heap[0])才push，
           并且push的时候要把原堆顶pop()出去，由于是最小堆，所以此时堆顶是当前扫描过后，堆中这k个元素中最小的那个
           而扫描完整个原数组后，每次只添加大于堆顶的，堆内又是排序的，堆顶为最小的，堆容量为k，故此时堆顶就是第
           k大的元素
        3. return
    复杂度分析：
        时间： NlogK,遍历数组ON，堆内浮动节点logK
        空间：OK，堆的长度
    """
    heap = []
    for i in range(len(nums)):
        if len(heap) < k:
            heapq.heappush(heap,nums[i])
        elif nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])
    return heap[0]
def findKthLargest(self, nums, k):
    import heapq
    """
    算法：第K大的元素就是第len(nums) - k + 1 小的元素，将数组堆化后pop() （len(nums) - k + 1 ）次就好
    复杂度分析：
        时间：应该是 KNlogN,最差N2logN（k==N）， 堆化：ON，弹出O1，弹出后整理应该是logN，因为元素要重新整理,整理K次，
        空间：ON，堆大小
    """
    heapq.heapify(nums)
    ans = None
    for i in range(len(nums) - k + 1):
        ans = heapq.heappop(nums)
    return ans
def findKthLargest(self, nums, k):
    import heapq
    """
    算法：排序后输出第k个元素即可
    复杂度分析：
        时间：NlogN，排序时间
        空间：O1
    """
    nums.sort(reverse=True)
    return nums[k - 1]
def findKthLargest(self, nums, k):
    import heapq
    """
    算法：内置函数直接返回，nlargset返回堆内前n个最大的数组成的列表，列表的最后一个[-1]就是答案
    复杂度分析：
        （点进去看，函数说明有一行 Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]）
        时间：NlogN,排序时间
        空间：O1
    """
    return heapq.nlargest(k, nums)[-1]
if __name__ == '__main__':
    print(findKthLargest([3,2,3,1,2,4,5,5,6],4))