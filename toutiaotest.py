import random
# def partition(nums,l,r):
#     pos = random.randint(l,r)
#
#     nums[l],nums[pos] = nums[pos],nums[l]
#     pivot = nums[l]
#     while l < r :
#         while l < r and nums[r] >= pivot:
#             r -= 1
#         nums[l] = nums[r]
#         while l < r and nums[l] < pivot:
#             l += 1
#         nums[r] = nums[l]
#     nums[l] = pivot
#     return l
#
# def quick_sort(nums,left,right):
#     if left < right:
#         p = partition(nums,left,right)
#         quick_sort(nums,left,p-1)
#         quick_sort(nums,p+1,right)
# def partition(nums,l,r):
#     pivot = nums[l]
#     while l < r:
#         while l < r and nums[r] >= pivot:
#             r -= 1
#         nums[l] = nums[r]
#         while l < r and nums[l] < pivot:
#             l += 1
#         nums[r] = nums[l]
#     nums[l] = pivot
#     return l




if __name__ == '__main__':
    n = 500
    print("BEFORE")
    nums = [random.randrange(n) for _ in range(n // 2)]
    #nums = list(range(100,-1,-1))
    print(nums)
    quick_sort(nums, 0, len(nums) - 1)
    print('AFTER')
    print(nums)
    print(sorted(nums))