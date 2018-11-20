#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def wiggleMaxLength( nums):
    """
    算法：贪心，上升序列or下降序列选择最后一个值(max or min)作为子序列值,选其为当前最优
    思路：
        首先分析最长摇摆序列是如何构成的，最好画图，将输入数组画折线图，可以发现数组是呈波动状态，
        分析：
            如果当前是上升状态，那么取上升状态中的最大的那个数，使扫描到后续数组中的数时成为摇摆序列的可能性最大，
            因为当前值最大，后面出现的就可能和他差值出现负数，满足摇摆序列的要求，下降状态同理
            这要注意如果nums[i]和nums[i-1]是相等的话，平着无波动，那么就应该跳过，或者说取它的最后一个状态，
            最后一个开始出现拐点，上升or下降的那个数为界
            ps:【这里用i和i-1是好算，用i和i+1也差不多的，毕竟算法思想是一样的，只是实现的细节不尽相同罢了】

        1. 如果长度<2，直接返回即可
        2. 因为要判断的是当前i和i-1的状态，故要初始化counter，判断头2个结点的关系，若头两个相等则取最后一个，否则counter就应该是2
           此时包含2个元素
        3. 遍历数组，记录历史差值和当前差值，当前差值和历史差值异号时出现拐点，counter+=1，注意，这里没有直接写diff * prevdif <=0
           的原因是，若diff * prevdif == 0，则diff和prevdiff都可能是0，但是注意，平坦的状态我们是不要的，即diff，所以不能直接写
           diff * prevdif <= 0 而要写 diff * prevdif <= 0 and diff != 0 ，或者分开来看 (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0)
    复杂度分析：
        时间：ON，扫描一遍数组
        空间：O1，常数级
    """
    if len(nums) < 2:
        return len(nums)
    prevdiff = nums[1] - nums[0]
    counter = 2 if prevdiff != 0 else 1
    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
            counter += 1
            prevdiff = diff
    return counter

def wiggleMaxLength_( nums):
    """
    算法：
        整体思想同上，检测peek转折点，但是这里构建一个状态机，扫描数组时，当前值与上一个值的关系无外乎三种，<,>,==，
        只有当状态从up到down或者down到up，或者begin2up,begin2down的时候，才会触发counter += 1
    """
    if len(nums) < 2:
        return len(nums)
    BEGIN = 0
    UP = 1
    DOWN = 2
    counter = 1
    state = BEGIN
    for i in range(1, len(nums)):
        if state == BEGIN:
            if nums[i] - nums[i - 1] > 0:
                state = UP
                counter += 1
            elif nums[i] - nums[i - 1] < 0:
                state = DOWN
                counter += 1
        if state == UP:
            if nums[i] - nums[i - 1] < 0:
                state = DOWN
                counter += 1
        if state == DOWN:
            if nums[i] - nums[i - 1] > 0:
                state = UP
                counter += 1
    return counter
if __name__ == '__main__':
    print(wiggleMaxLength([1,3,4,4,4,]))