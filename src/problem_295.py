#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import heapq
class MedianFinder(object):
    """
    算法：双堆
    思路：找中位数就是找中间的两个数A,B，或中间那一个数A，A之前的数都小于A，B之后的数都大于A，且AB位于数组中间位置
    那么可以利用大顶堆小顶堆的特性来维护两个堆，每个堆的元素都应该是整个数组的half，或者其中一个half+1，保持大顶堆的
    顶部及最大值是小于小顶堆的顶部即最小值，这样两个堆的堆顶即是中位数故：
        1. 维持一个大顶堆，一个小顶堆
        2. 在元素添加的时候，先将元素添加到大顶堆，再从大顶堆pop堆顶添加到小顶堆中，如果小顶堆长度大于了大顶堆，将
           小顶堆的堆顶弹出加入到大顶堆中，这样保障总是保持大顶堆之多比小顶堆多一个元素
        3. 返回中位数的时候直接计算即可
    复杂度分析：
        时间：OlogN，堆挪动元素的时间耗费
        空间：ON，两个堆所占用的空间大小
    """
    def __init__(self):
        # keep smaller half (size >= 1)
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        return ((-self.maxHeap[0] + self.minHeap[0] + 0.00) / 2)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()