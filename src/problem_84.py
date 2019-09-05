#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def largestRectangleArea( height):
    """
    https://www.jianshu.com/p/2e5edb21d0ff
    Disscussion Method
    算法：单调栈
    思路：
        首先要明确所有可能的面积都是以某个矩形的高度为高而产生的矩形面积
        目标就是在所有这些矩形高度为height的矩形面积中找到最大的那个
        注意到原数组内的元素是无序的，所以不能直接用动规那些，而且为了求矩形面积，也不能将数组内的元素排序

        所以可以用单调栈来维护一个栈内元素单调递增的栈，并且根据栈内的元素求矩形的面积
            以某个height做矩形高的矩形，一定是当前这个矩形是最低的了，即左右都没有比他更低的元素，
        比如示例图中的[2,1,5,6,2,3]，对5来说，右侧第一个小于5的是2，以5为高的矩形，右边界最大也就到2的下标，
        然后再看height中左侧第一个小于5的是哪里，比如是1，那么想要5做高的话，就得1到2的下标之差做长，这样才可以计算出来
        以5为高的矩形面积！这种思想有点像求前k大的数，但是保留一个小顶堆一样
        所以维护单调栈内的元素递增，对height进行遍历，如果当前元素大于栈顶，那么将当前元素下标入栈，否则说明当前元素
        小于栈顶，而栈内元素又是递增的，则：
            栈顶元素对应的高度就是当前要计算的矩形高
            h = heights[stack.pop()]
            此时的index = stack[-1]是左侧第一个小于高度h的元素的下标，此时遍历到的下标i是右边第一个小于高度
        h的元素的下标，那么以h为高的矩形，宽度w就是i-stack[-1]-1，然后更新ans = max(ans,w * h)

        ❗️❗️❗️：
            一定要理解到，当前的i是右侧第一个小于h的下标，stack[-1]是左侧第一个小于h的下标，所以求以h为高的矩形
        面积的时候，要把左侧和右侧的下标都找到才行！就像[2,1,2]，ans = 3，就是以1为h，3为w

        这里有两个Trick：
            1. stack=[-1]保持stack内总是有元素的且总有元素是小于任何一个位置的，方便当stack内只剩下来自heights的
            一个元素时，计算w,选用-1是因为，heights中的元素都是非负的，所以左侧用-1就可以保证是一个小于所有heights
            内元素的值,stack内是下标的概念，-1是为了最后总能有一个最左侧的下标，不能取0，取0的话相当于取第一位元素！
            而且根据第二个trick，一开始的时候stack[-1]指向的正是height = 0。而所有元素都是大于0的

            2.heights.append(0)，保持heights中最末尾总有一个小于所有元素的，这样才可以在heights都append到stack后
            通过最末尾的这个0将stack中剩下的元素对应的面积全部求出来，
    """
    height.append(0)
    stack = [0]
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:
            index = stack.pop()
            h = height[index]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans
if __name__ == '__main__':
    print(largestRectangleArea([2,1,5,6,2,3]))
