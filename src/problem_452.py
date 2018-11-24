#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findMinArrowShots0(self, points):
    """
    算法：贪心
    思路：
        贪心：从当前位置发射，射穿当前气球的时候尽可能地多射穿后面的气球
            画图观察可以看到，若两个区间可以用同一发子弹击穿，那么二者一定是有公共区间段的
        如此便可以将问题转化为，给定的这些区间，最少可以提取出多少个公共子区间段
        （当我自己画图的时候我注意到我其实是从小到大一根线一根线去画的，所以很自然地联想
        到要先将线段根据线段的start排序后处理）
        最优子结构：
            将线段【排序】后依次开始判断，可以看到，当前区间总是和上一个区间在比较，可以联想
        到当前线段是否需要新的一发子弹仅取决于它是否与上一个区间有重合部分，有的话那么就不需要
        新的子弹，无重合部分的话则需要新的一发。（排序后由于是依次添加进去的，所以可以将已经
        求得公共区间的部分看做是一个整体，即A，B的公共区域C看做是一个新的区间，而原A和B就可以
        舍弃了，用C作为一个新的区间去和后面判断）
            排序后问题具有了最优子结构，那么就可以一层一层地解决该问题，判断当前区间和上一个区间
        有没有重合部分，有的话计数器不变，并且更新新的区间起始位置为当前两个线段的重合部分
        否则的话计数器+1，并且另完整的当前区间作为下一个区间比较时的上一个区间，即behind=curr
    复杂度分析：
        时间：ONlogN，排序NlogN，遍历ON
        空间：O1，常数级
    """
    if points == []:
        return 0
    points.sort(key=lambda x: x[0])

    counter = 1
    behind = points[0]
    for i in range(1, len(points)):
        curr_ball = points[i]
        if curr_ball[0] <= behind[1]:
            start = max(curr_ball[0], behind[0])
            end = min(curr_ball[1], behind[1])
            behind = [start, end]
        else:
            counter += 1
            behind = curr_ball
    return counter

def findMinArrowShots1(points):
    """
    算法：贪心
    思路：
            类似于上面的findMinArrowShots0，但是这里排序排的是区间段的右值，核心思想是，先设置弓箭手
        位置初始化为points[0][1]即右值最小的那个位置，然后一次判断新的区间与当前弓箭手位置的关系
        由于已经排序过了，后面的区间段的右端值一定大于当前弓箭手的位置，那么如果两个区间有重叠，则当前
        待判断区间的左值一定<=当前弓箭手的位置，否则的话就说明这个区间的start 大于弓箭手的位置，且右值end
        也大于弓箭手的位置，这就表明需要在这个区间位置新添加一个弓箭手，则新弓箭手的位置=points[i][1],
        持续遍历直到所有区间判断完。
            这样也是有最优子结构和贪心的思想在的，贪心的思想就是我当前位置的弓箭手要尽可能多地射气球，所以
        只要有重合区间就不射新的弓箭手，和我的上一个方法相比其实主要区别就在于判断重合区间段的方式不同了，
        这种方法写出来代码更简洁，在最优子结构上，即是判断完当前区间的重合情况后就可以把AB融合为C来看，
        就像上面的findMinArrowShots0一样
    复杂度分析：
        时间：ONlogN，排序，遍历一次
        空间：O1，常数级
    """
    if points == []:
        return 0
    points.sort(key=lambda x: x[1])
    counter = 1
    arrow_pos = points[0][1]
    for i in range(1, len(points)):
        if arrow_pos >= points[i][0]:
            continue
        counter += 1
        arrow_pos = points[i][1]
    return counter
"""
是有问题的，不排序的话，只是按原无序状态去求公共区间，会存在不满足最优子结构的性质，
即不可以将已经形成公共区间外的段扔掉，而排序后由于是依次添加进去的，所以可以将已经
求得公共区间的部分看做是一个整体，即A，B的公共区域C看做是一个新的区间，而原A和B就可以
舍弃了，用C作为一个新的区间去和后面判断。

def findMinArrowShots1(points):
    
    if points == []:
        return 0
    counter = 1
    exist = [points[0]]
    for i in range(1, len(points)):
        curr_ball = points[i]
        found = False
        for j in range(len(exist)):
            exist_ball = exist[j]
            if (curr_ball[0] >= exist_ball[0] and curr_ball[0] <= exist_ball[1]) or (exist_ball[0] >= curr_ball[0] and exist_ball[0] <= curr_ball[1]):
                exist_ball[0] = max(curr_ball[0], exist_ball[0])
                exist_ball[1] = min(curr_ball[1], exist_ball[1])
                found = True
                break
        if not found:
            counter += 1
            exist.append(curr_ball)
    return counter
"""
if __name__ == '__main__':
    print(findMinArrowShots1([[10,16], [2,8], [1,6], [7,12]]))