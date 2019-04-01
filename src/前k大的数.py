#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random
def biggest_k(nums,k):
    import heapq
    if k >= len(nums):
        return nums
    heap = []
    for i in range(len(nums)):
        if len(heap) < k:
            heapq.heappush(heap,nums[i])
        elif nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,nums[i])

    return heap
if __name__ == '__main__':
    n = 1000000
    k = 10
    nums = [random.randrange(n) for _ in range(n // 2)]
    print(sorted(biggest_k(nums,k),reverse=True))
    nums.sort(reverse=True)
    print(nums[:k])