#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def groupAnagrams( strs):
    """
    My Method
    算法：哈希表映射
    思路：
            首先确定"Anagrams"词的特征：长度一样，组成的各字符一样，各字符出现的数量一样
            其实只要满足一点就可以，26个字母出现的计数值一样，Anagrams词可以放在一个桶内
            很容易想到用hash_map去做，关键是如何构成hash_key
            可以对26个字母建一个[0]*26的列表，然后依次统计每个字符出现的次数，将统计后的结果
        转化为不可变对象，就可以作为hash_key来映射了
        注意：
            1. 字符串是可以sorted()的，虽然字符串对象没有.sort()方法，但是可以用sorted()函数进行排序，返回排序后的字符俩表
            2. 不一定非要连接为字符串去做key，tuple也一样的
            3. 返回return的时候，不用新建一个列表[]去存储hash_map的v，直接list(hash_map.values())就好啦！
    复杂度分析：
        时间：ONK，对N个string遍历，对每个string也要遍历，k是string中的最大长度
        空间：ONK，hashmap的存储空间
    """
    # 还要求同一个字母出现的个数是相同的才可以！
    hash_map = {}
    for string in strs:
        char_count = [0] * 26
        for char in list(string):
            char_count[ord(char) - ord('a')] += 1
        hash_key = tuple(char_count)
        hash_map.setdefault(hash_key, [])
        hash_map[hash_key].append(string)
    return list(hash_map.values())
    # 或者
    # char_count = [str(count) for count in char_count]
    # hash_key = tuple(char_count)
    # 也可以，key需要是不可变对象就行！

def groupAnagrams1( strs):
    """
    算法：哈希表映射
    思路：
        与My Method类似，只不过这里讲字符串排序后组成的tuple构成键！
        字符串是能用sorted()方法排序的！返回排序后的字符列表！
    复杂度分析：
        时间：ONKlogK，对N个string遍历，对每个string要排序消耗KlogK
        空间：ONK，hashmap的存储空间
    """
    # 还要求同一个字母出现的个数是相同的才可以！
    hash_map = {}
    for string in strs:
        hash_key = tuple(sorted(string)) #或者 hash_key = ''.join(string_list) 也行
        hash_map.setdefault(hash_key, [])
        hash_map[hash_key].append(string)
    return list(hash_map.values())
if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))