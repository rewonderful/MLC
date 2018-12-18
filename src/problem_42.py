#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def trap(self, height):
    """
    My Method
    算法：左右指针
    思路：
        思路类似于407题，想象水从周围一点一点漫上去，涨起来~
            对某个位置i来说，其能容积多少水，取决于左右两侧的墙的高度重最小的那个高度
            而对整个容器来说，取决于整体两侧墙的最短的那个，所以设立左右指针left，right，哪侧墙矮就从哪侧
        来计算，left小就判断left和left+1的height，如果height[left] > height[left+1],那么就可以盛
        height[left]-height[left+1]这么多的水，并且要将height[left+1]更新为盛满水后的的高度，当然，
        如果height[left+1]本就大于等于height[left]，自然就不用更新了，同理，对于右侧right部分也是做同样的
        计算，直至left >= right，因为left和right肯定要隔着1个，如果left == right，那left和right间就没有
        间隔了，就不该算了
    复杂度分析：
        时间：ON，遍历一次数组
        空间：O1，常数级
    """
    if height == []:
        return 0
    left = 0
    right = len(height) - 1
    result = 0
    while left < right:
        if height[left] <= height[right]:
            result += max(0, height[left] - height[left + 1])
            height[left + 1] = max(height[left], height[left + 1])
            left = left + 1
        else:
            result += max(0, height[right] - height[right - 1])
            height[right - 1] = max(height[right], height[right - 1])
            right = right - 1
    return result