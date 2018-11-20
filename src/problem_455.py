#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findContentChildren(self, g, s):
    """
    算法：贪心
    思路：
        贪心的思路是当前问题具有最优子结构，当前问题能被分解为规模更小的子问题，且当前最优解（局部最优解）加上规模更
        小问题的最优解就是全局最优解，每一步都做贪婪选择，做一个"最"值选择，本题中，分配给孩子糖果就是一个贪心的思路，
        拿糖果去试孩子的"贪婪度"，将孩子按"贪婪度"从小到大排序，拿糖果一个一个去试，从最小的糖果开始，每个糖果只试一次
        如果当前糖果能满足该孩子，那么久assign，否则的话拿下一个糖果去试该孩子，即，将糖果从小到大开始去试，先满足"贪婪度"
        较低的孩子。如果能满足了该孩子，那么加一个，不能的话再拿后面的糖果去试blabla
    复杂度分析：
        时间：NlogN，排序NlogN，遍历一次ON
        空间：O1，常数级
    """
    if len(s) == []:
        return 0
    g.sort()
    s.sort()
    child = 0
    cookie = 0
    while cookie < len(s) and child < len(g):
        if g[child] <= s[cookie]:
            child += 1
        cookie += 1
    return child