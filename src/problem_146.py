#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
    My Method
    算法：双向链表+字典
    思路：
        首先一定要回顾一下LRU算法，其实就是一个优先队列，最近使用过的在队尾，时间久的在队头，该队列
    是有长度限制的，超出长度后最久未访问的元素出队列，类似于一种先进先出。然后访问元素的时候，要将
    该元素设为最近访问过的元素
        我这里就设队头代表最近最久未访问，队列尾代表最近访问的元素
        很容易想到用线性表去做，但是也很容易发现，用线性表的话在get调整元素位置的时候会挪动大量的元素，
    导致时间效率很低，这个时候可以很容易想到用链表结构去做，用链表的话将一个元素拆下来放到队列尾是O1的
    时间复杂度，所以只要设置一个队列头指针head和一个尾指针tail就OK了，因为拆卸链表需要知道节点的前驱，
    所以用双向链表来记录节点的情况，同时需要设立一个字典dict记录节点的内存地址，达到get时快速访问的目的。
        因此可以将LRU描述为用含head和tail指针的队列进行put，get操作
            get时：
            key在dict中时，将节点remove掉，再append回队列，就完成了node的位置调整
            put时:
            要注意同key的node更新，也是先将节点remove掉，然后再append进来，只不过append的时候要改一下node.val
            不同key的话：
                先要考虑队列是否满，队列长度满则弹出队首，否则的话计数加一，然后都要append新的node
        所以要建立啊remove和append的辅助函数进行操作
            remove拿到node的前驱就可以正常删了，但是要注意node可能是tail，所以要将self.tail更新为前一个位置！
            append的话就比较直观了，在self.tail后面追加这个node即可
        再一个就是不要忘记删除节点和添加节点的时候要更新dict
    复杂度分析：
        时间：O1
        空间：ON

"""
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = ListNode(0, 0)
        self.tail = self.head
        self.node_dict = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.node_dict:
            node = self.node_dict[key]
            node = self.del_node(node)
            self.append(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.node_dict:
            node = self.node_dict[key]
            node = self.del_node(node)
            node.val = value
            self.append(node)
            return
        if len(self.node_dict)== self.capacity:
            self.node_dict.pop(self.head.next.key)
            self.del_node(self.head.next)
        node = ListNode(key, value)
        self.append(node)
        self.node_dict[key] = node

    def del_node(self, node):
        if node == self.tail:
            self.tail = node.pre
        pre = node.pre
        next = node.next
        pre.next = node.next
        node.pre = None
        node.next = None
        if next != None:
            next.pre = pre
        return node

    def append(self, node):
        self.tail.next = node
        node.next = None
        node.pre = self.tail
        self.tail = self.tail.next
"""
----------------------------------------------------------------
    Disscussion Method 1
    
        其实我也是看了Disscution后弃用了单链表，不过之前我的做法中用单链表+dict存储pre和双向链表也差不多，还不如
    直接双向链表更加直接。
        下面的这个方法是设立了两个哑节点headdummy和taildummy，而我的方法是head是dummy，tail是指向
        实在的元素的，他这种写法也是比较简洁的
        dummyhead-->1-->2-->3-->4-->taildummy
        而我的是:
        dummyhead-->1-->2-->3-->4
                                ^
                                |
                                tail
    其实他这种两个dummy的可能看起来会更方便一些，我这种的话tail每次要栋，而dummytail的话就像dummyhead一样
    dummyhead.next是真实的head
    dummytail.prev是真实的tail
"""
class Node(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache1(object):

    def __init__(self, capacity):
        self.dic = {}
        self.capacity = capacity
        self.dummy_head = Node(0, 0)
        self.dummy_tail = Node(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key):
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.append(node)
        return node.val

    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key, value)
        self.append(node)
        self.dic[key] = node

        if len(self.dic) > self.capacity:
            head = self.dummy_head.next
            self.remove(head)
            del self.dic[head.key]

    def append(self, node):
        tail = self.dummy_tail.prev
        tail.next = node
        node.prev = tail
        self.dummy_tail.prev = node
        node.next = self.dummy_tail

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

"""
----------------------------------------------------------------------------

    Disscussion Method 2
    
    Do as they say
    算法：小顶堆
    思路：
            用优先队列，or 堆来保持LRU的状态，就像do as they say一样，用time来保存时间戳，利用最小堆通过时间戳
        的大小来保存当前应当替换的页面key
            这样思路就比较直观了
            用dic去存储时间戳和key,value,dict[key] = (time,value)
            所以当get的时候，就判断key in dict or not，在的话就返回value并更新dict中存储的key的时间戳
            put的时候，也是先判断key如果在dic中，就更新dict[key]中的时间戳为最新的
            不在put中的话同样先判断len(dic) > capacity or not,
                要做一些【清理工作】
                    具体来说就是检查有没有节点的时间戳在后面get 或者put的时候被更新了，因为最小堆不像链表一样
                可以直接找到节点的位置并且拆卸下来，所以这种思路就是曲线去找，如果当前应该弹出的堆顶元素发现
                其实后面被更新过了，堆顶的时间戳time和dict[key]中存储的时间戳不一样，那么久更新堆顶元素，
                一直更新直到找到一个元素确实是最小堆堆顶该弹出，就把他弹出就好了，heapq.pop,并且记得要del dict[key]
            然后push新的时间戳的key，value就好了
    复杂度：
        时间：OK，K是队列长度，肯定不是O1，get是O1，put不是O1，因为要做清理工作，但是至多对队列内所有的K个元素每个都更新
        一次，所以OK，效率也还是挺高的
"""

from time import time
import heapq

class LRUCache2:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.hp = []  # (pre,vale)
        self.dic = {}  # (now, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:  # never exits before
            return -1
        pre, val = self.dic[key]
        new = time()
        self.dic[key] = (new, val)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        now = time()
        if key in self.dic:
            self.dic[key] = (now, value)
            return
        if len(self.hp) >= self.cap:
            self.clean()
        self.dic[key] = (now, value)
        heapq.heappush(self.hp, (now, key))

    def clean(self):
        while (True):
            (pre, key) = self.hp[0]
            (new, value) = self.dic[key]
            if new > pre:
                heapq.heapreplace(self.hp, (new, key))
            else:
                heapq.heappop(self.hp)
                del self.dic[key]
                return
if __name__ == '__main__':
    """
    ["LRUCache","put","get","put","get","get"]
    [[1],[2,1],[2],[3,2],[2],[3]]
    """
    cache = LRUCache(1)
    cache.put(2, 1)
    cache.get(2)
    cache.put(3, 2)
    cache.get(2)
    cache.get(3)
    # cache = LRUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # cache.get(1)
    # cache.put(3, 3)
    #
    # cache.get(2)
    # cache.put(4, 4)
    #
    # cache.get(1)
    # cache.get(3)
    #
    # cache.get(4)
