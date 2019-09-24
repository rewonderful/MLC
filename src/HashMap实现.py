#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class HashTable:
    def __init__(self):
        # 初始化两个list，一个用来保存键值，一个用来保存值
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # 定义Hash函数，使用余数法
    def hashFunction(self, key, size):
        return (key % size)

    # 定义线性探测hash函数
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    # 插入键值对
    def put(self, key, data):
        # 　得到Ｈａｓｈ值
        hashvalue = self.hashFunction(key, len(self.slots))
        # 查找当前hash值对应位置的键值是否为空，为空则插入
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        # 不为空则更新
        else:
            nextslot = -1
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                # 否则继续查找下一个位置，这里使用线性探测器去解决Hash冲突问题
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data

    # 重载Python的magic函数
    def __getitem__(self, key):
        return self.get(key)

    # 重载Python的magic函数
    def __setitem__(self, key, data):
        self.put(key, data)

    # 拿键值方法和存放方法一样
    def get(self, key):
        startslot = self.hashFunction(key, len(self.slots))

        data = None
        flag = False
        stop = False
        pos = startslot

        while self.slots[startslot] != None and not flag and not stop:
            if self.slots[pos] == key:
                flag = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, len(self.slots))
                if pos == startslot:
                    stop = True
        return data


if __name__ == '__main__':
    H = HashTable()
    H[54] = 'cat'
    H[26] = 'dog'
    H[93] = 'lion'
    H[17] = 'tiger'
    H[77] = 'bird'
    H[31] = 'cow'
    H[44] = 'goat'
    H[55] = 'pig'
    H[20] = 'chicken'
    H[8] = 'mouse'
    H[54] = 'mycat'

    print(H.slots)
    print(H.data)