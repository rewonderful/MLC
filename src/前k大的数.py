# #!/usr/bin/env python
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
def quick_index(nums,lo,hi):
    pivot  = nums[lo]
    while lo < hi:
        while lo < hi and nums[hi] <= pivot:
            hi -= 1
        nums[lo] = nums[hi]
        while lo < hi and nums[lo] > pivot:
            lo += 1
        nums[hi] = nums[lo]
    nums[lo] = pivot
    return lo


def topk_biggest(nums,k):
    lo,hi = 0, len(nums)-1
    # index = quick_index(nums,lo,hi)
    # while index != k:
    #     if index < k:
    #         index = quick_index(nums,index+1,hi)
    #     else:
    #         index = quick_index(nums,lo,index-1)
    # return nums[:k]
    index = quick_index(nums,lo,hi)
    while index != k:
        if index < k:
            index = quick_index(nums,index + 1,hi)
        else:
            index = quick_index(nums,lo,index - 1)
    return nums[:k]
    # while lo < hi:
    #     index = quick_index(nums, lo, hi)
    #     if index == k:
    #         return nums[:k]
    #     elif index < k:
    #         lo = index + 1
    #     else:
    #         hi = index - 1

if __name__ == '__main__':
    n = 1000000
    k = 10
    nums = [random.randrange(n) for _ in range(n // 2)]
    print("heap: ",sorted(biggest_k(nums,k),reverse=True))
    print("quick_index: ",topk_biggest(nums,k))
    nums.sort(reverse=True)
    print(nums[:k])