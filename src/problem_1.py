nums = [2, 3, 3, 3]
target = 6

n = len(nums)
#创建一个空字典
d = {}
for i in range(n):
    a = target - nums[i]
    #字典d中存在nums[x]时
    if nums[i] in d:
        print( d[nums[i]],i)
    #否则往字典增加键/值对
    else:
        d[a] = i

# n = len(nums)
# for x in range(n):
#     a = target - nums[x]
#     if a in nums:
#         y = nums.index(a)
#         if x == y:
#             continue
#         else:
#             print (x,y)
#             break
#     else :
#         continue

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """










dict = {}
#counter = 0
# for element in list:
#     dict[element] = counter
#     counter += 1
# for key in dict:
#     num1 = key
#     num2 = target - num1
#     if num2 in dict: #and dict[num2]!= dict[num1]:
#         print(dict[num1],dict[num2])
