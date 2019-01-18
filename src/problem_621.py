#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def leastInterval(self, tasks, n):
    """
    Solution Method
        从举例子中我们可以得出任务调度的规律。
    如给定：AAABBCD，n=2。那么我们满足个数最多的任务所需的数量，即可以满足任务间隔要求，即：AXXAXXA；
    （其中，X表示需要填充任务或者idle的间隔）

        如果有两种或两种以上的任务具有相同的最多的任务数，如：AAAABBBBCCDE，n=3。那么我们将具有相同个数的任务
    A和B视为一个任务对，最终满足要求的分配为：ABXXABXXABXXAB，剩余的任务在不违背要求间隔的情况下穿插进间
    隔位置即可，空缺位置补idle。

        由上面的分析我们可以得到最终需要最少的任务时间：
            ans = （最多任务数-1）*（n + 1） + （相同最多任务的任务个数）。
    有上面的例子来说就是：(num(A)-1) * (3+1) + (2)。

        但是还有一种情况是ans 会 < tasks的数量，len(tasks) > ans，这就意味着有任务没有安排完，所以还要判断一下len(tasks)
        和这样计算后的ans，取较大的哪一个
        👆至于为什么这样，好像有证明可以证明，但是没了解了

    """
    counter = [0] * 26
    for task in tasks:
        counter[ord(task) - ord('A')] += 1

    max_num = 0
    max_need = max(counter)
    for count in counter:
        if count == max_need:
            max_num += 1
    return max(len(tasks), (max_need - 1) * (n + 1) + max_num)