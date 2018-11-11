#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def findDuplicate(self, nums):
    """
    快慢指针法：
        分析：
             首先这道题可以画一个"状态机"，数组值就是状态，由于有重复的元素，那么整个数组画起来
             就会变成一个有环的状态机结构，那么整个问题就转化为了，判断环出现位置的结点，类似142题

        算法：
            数组长度是n+1,数组内的数字都是[1,n]的，即下标（除0外）都可以一一映射为数组内的一个个元素
            据此可以根据下标到元素值的映射构造出一个链表一样的结构，i->nums[i]，nums[i]->i，i->nums[i]...
            在这样的结构下，下标0可以看做是数组的head节点(但此head非哑节点，它还是有用的)
            据此，可以将数组转化为"链表"结构，i从0开始计算元素值nums[i]，以nums[i]为下标计算下一个nums[i]，
            类比于链表的p.next,这里的next就由nums[nums[i]]来表示，但是要判断的还是一个个的nums[i]值，
            即元素值。转化为快慢指针后同142题，快指针每次2步走，慢指针每次1步走，相遇时用于一个新的指针从
            头结点0处出发一次1步，slow也一次1步出发，再次相遇时的值即为重复值，亦环结点处
        复杂度：
            时间： On，和问题规模与问题自身有关
            空间： 01，fast,slow,p的空间，常数级
    """
    fast = 0
    slow = 0
    fast = nums[nums[fast]]
    slow = nums[slow]
    while fast != slow:
        fast = nums[nums[fast]]
        slow = nums[slow]
    p = 0
    while p != slow:
        p = nums[p]
        slow = nums[slow]
    return p