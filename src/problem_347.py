#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import collections
import heapq


def topKFrequent_(self, nums, k):
    """
    python的counter对象是有直接的内建方法拿到most_common元素的
    """
    dic = (collections.Counter(nums))
    lt = dic.most_common(k)
    ret = []
    for x, y in lt:
        ret.append(x)
    return ret
def topKFrequent0(self, nums, k):
    """
    Solution Method
    掉包，用collections的counter统计
    用heapq的nlagest返回第K大的数，然后key是count.get，也就是依据频率
    """
    count = collections.Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
def topKFrequent(self, nums, k):
    """
    My Method 1
    算法：哈希表+堆
    思路：
        用哈希表统计频率，建立大顶堆，堆内元素是(频率，key)，弹出前K个元素即可
        然后要注意的是一个小tricky，python的heapq只能对单个元素进行建堆，所以要把频率放在前面，
        否则会按照key的大小作为优先级的依据进行建堆，
        大顶堆通过给频率加负号来实现
    """
    import heapq

    record = {}
    for num in nums:
        record.setdefault(num,0)
        record[num] += 1
    heap = []
    for key,value in record.items():
        heapq.heappush(heap,(-value,key))
    ans = []
    for i in range(k):
        ans.append(heapq.heappop(heap)[1])
    return ans


def topKFrequent1(self, nums, k):
    """
    同上，不同的是这里是排序后取前K个
    """
    record = {}
    for num in nums:
        record.setdefault(num, 0)
        record[num] += 1
    heap = []
    for key, value in record.items():
        heap.append((key, value))
    tmp = sorted(heap, key=lambda x: x[1], reverse=True)
    ans = []
    for i in range(k):
        ans.append(tmp[i][0])
    return ans


if __name__ == '__main__':
    print(topKFrequent([1,1,1,2,2,3,3,3,3,3],2))