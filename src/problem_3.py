#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def lengthOfLongestSubstring(s):
    """
    算法：时间窗口+哈希表
    思路：
            设置begin指针和i指针，在begin与i之间的连续字符串就是s的一个子串
            i依次向后移动，begin记录的是无重复子串的初始位置，哈希表记录字符最近的出现在列表中的位置(下标)
            借助哈希表来判断当前位置curr的字符char是否已经出现过了，如果未出现那么当前子串sub就是s[begin,i]
        计算i-begin+1就是子串sub的长度，用max去比较是否是最大的，然后更新
            那么如果i指向的curr已经在哈希表中出现时，首先要注意，要判断curr所代表的过去的位置与begin的位置，只有
        当该字符记录中的位置position[curr]大于等于当前begin的位置时，才应该更新begin的位置，并且更新position[curr
        的位置为当前的位置，更新到最新。因为我们的窗口是从后往前移的，begin的位置只能更大，不能跑到前面去！
            譬如：
                abba，如果不设置position[curr] >= begin的条件，当i=3时，begin会跑到0去，误认为子串是abba，这样
                最大子串长度就成了4，这样是不符合要求的！begin的位置只能往后挪，不能往前挪！
            更新begin的位置时将其位置更新到重复字符的后一个位置即可，这样新的当前子串中就没有重复子串了
    复杂度分析：
        时间：ON，遍历一遍字符串
        空间：ON，线性空间
    """
    max_len = 0
    begin = i = 0
    position = {}
    while i < len(s):
        curr = s[i]
        if curr in position and position[curr] >= begin:
            begin = position[curr] + 1
            position[curr] = i
        else:
            position[curr] = i
        max_len = max(max_len, i - begin + 1)
        i += 1
    return max_len

def lengthOfLongestSubstring2(s):
    """
    My Method
    算法：队列窗口
    思路：
        挨个遍历字符串中的字符，设置一个队列记录最长不重复子串
        当新字符没有出现在队列中时，即无重复，就队尾添加元素
        否则找到重复元素的位置index，更新queue为queue[index+1:]
        计算当前queue的长度即最大无重复子串的长度，更新
    复杂度分析：
        时间：ON2，遍历一遍字符串，queue.index()操作是ON，所以ON2
        空间：ON，线性空间
    """
    max_len = 0
    queue = []
    for char in s:
        if char in queue:
            index = queue.index(char)
            queue = queue[index + 1:]
        queue.append(char)
        max_len = max(len(queue), max_len)
    return max_len

if __name__ == '__main__':
    #print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("abba"))




