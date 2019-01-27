#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    Disscussion Method
    用哈希表和数组来记录元素
    用哈希表的特性来快速的add和remove，用list的特性来快速的get

    哈希表内存的元素是，key就是目标的val，value是val在list中的下标，即索引
    所以add的时候很好说，get的时候也是，只要引入random来产生一个随机下标就好了

    关键是remove
    remove的时候要对list和dict都做处理达到O1的时间，Disscussion中这种做法的巧妙之处就在于
    先通过map得到要删除的val的下标pos，然后在将list[pos]的值由要删除的val改写成list[-1]，这样一来就相当于
    删除了val，然后list再POP，因为pop是O1的，然后再在map中将原list的最后一个位置的值的下标索引在map中更新
    为pos即可
"""
class RandomizedSet:
    import random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            self.list.append(val)
            self.map[val] = len(self.list) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            pos = self.map[val]
            last = self.list[-1]

            self.list[pos] = last
            self.map[last] = pos

            self.map.pop(val)
            self.list.pop()
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.list[random.randint(0, len(self.list) - 1, )]