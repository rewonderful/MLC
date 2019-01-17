#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxSlidingWindow(self, nums, k):
    """
    Disscussion Method
    算法：单调双向队列
    思路：
            和单调栈类似，单调栈是栈内元素保持某种单调性，单调双向队列是队列内保持某种单调性，然后由于本题的背景，
        所以使用双向队列
            首先要明确➡️单调队列保持队列内有序
            用一个单调队列来记录遍历过的值的下标
            比如1，3，2，0遍历到3的时候，由于3进来后，前面比3小的元素一定不可能是目标的元素，所以将其弹出，而遍历
        到2的时候，2不大于3，并且不知道2后面的元素会不会比2更小，也就是2可能是一个候选的最大值，所以入队列。如此
        一来便可以在遍历到第i个元素时确认这个元素的留存状态，即它大于队列尾元素，队列尾弹出，然后第i元素入队列。
            这个队列的长度可以和要求的k不相干，其实也是相干的，len(queue)应该不大于k，但是这是个很弱的条件，
        事实上经过上面描述的这种入队列方式后队列内保障了队首元素就是当前队列内的最大的那个元素，但是由于它是保持
        了一系列的历史值，所以可能队首元素实际上已经不在窗口限制的K的范围内了，如上面这个例子如果窗口长度是2的话，
        即使遍历到0的时候，最大值应该是2了，这个时候就应该弹出队首，这个是硬条件-->队首元素在窗口外，就要弹出队首
        所以队列内记录的是下标。
            然后就是当i的范围在完整窗口长度建立后即i>=k-1时才append到ans中
    """
    ans = []
    from collections import deque
    queue = deque()
    for i in range(len(nums)):
        while queue and queue[0] < i - k + 1:
            queue.popleft()
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        queue.append(i)
        if i >= k - 1:
            ans.append(nums[queue[0]])
    return ans
def maxSlidingWindow1( nums, k):
    """
    暴力解法
    """
    if k > len(nums):
        return [max(nums)]
    n = len(nums) - k + 1
    ans = []
    for i in range(n):
        silidingWin = nums[i:i + k]
        ans.append(max(silidingWin))
    return ans
if __name__ == '__main__':
    print(maxSlidingWindow([1, 3, 1, 2, 0, 5],3))