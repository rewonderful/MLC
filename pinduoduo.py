# #!/usr/bin/env python
# # _*_ coding:utf-8 _*_
# import random
# # def partition(nums,l,r):
# #     pivot = nums[l]
# #     while l<r:
# #         while l<r and nums[r] >= pivot:
# #             r -= 1
# #         nums[l] = nums[r]
# #         while l < r and nums[l] < pivot:
# #             l += 1
# #         nums[r] = nums[l]
# #     nums[l] = pivot
# #     return l
#
#
# def quick_sort(nums,lo,hi):
#     if lo < hi:
#         l ,r = lo,hi
#         pivot = nums[l]
#         while l<r:
#             while l<r and nums[r] >= pivot:
#                 r -= 1
#             nums[l] = nums[r]
#             while l < r and nums[l] < pivot:
#                 l += 1
#             nums[r] = nums[l]
#         nums[l] = pivot
#         quick_sort(nums,lo,l-1)
#         quick_sort(nums,l+1,hi)
# if __name__ == '__main__':
#     n = 50
#     print("BEFORE")
#     nums = [ random.randrange(n) for _ in range(n//2)]
#     print(nums)
#     quick_sort(nums,0,len(nums)-1)
#     print('AFTER')
#     print(nums)
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# def binarySearch(nums,target):
#     low = 0
#     high = len(nums)-1
#
#     while(low <= high):
#         mid = int((low + high) / 2)
#
#         if target == nums[mid]:
#             return mid
#         if target > nums[mid]:
#             low = mid+1
#         else:
#             high = mid - 1
#     return 0
# def binarySearch(nums,target):
#     lo ,hi = 0,len(nums)-1
#     while lo <= hi:
#         mid = (lo+hi)//2
#         if mid == target:
#             return mid
#         elif nums[mid] < target:
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     return -1
#
#
# if __name__ == '__main__':
#     nums = [1,2,3,4,5,9,11,13,222,333,444,555]
#     target = 5
#     print(binarySearch(nums,target))
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def merge(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums)//2
    left_part = merge(nums[:mid])
    right_part = merge(nums[mid:])
    return mergesort(left_part,right_part)

def mergesort(left,right):
    i ,j = 0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result


if __name__ == '__main__':
    print(merge([9,8,7,6,5,4,3,2,1,0]))
    #print(mergesort([1,5,7],[2,4,6]))
