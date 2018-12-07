#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def wordPattern( pattern, str):
    """
    算法：哈希表映射
    思路：
        将patter与str建立一对一的哈希表映射，
        逐个遍历patter与str，若某个patter的char第一次出现，则建立它与string的一一映射关系。
        如果char已经有了或者string已经有了，就去检查当前的string或char与一一对应的哈希表中
        存储的char2sting[char]或者string2char[string]是否相等，如果相等那没事，不相等的话
        说明出现了不符合模式的情况，return False
        遍历完成都通过的话return True
    复杂度分析：
        时间：ON，遍历一次pattern
        空间：ON，字典，辅助list的空间
    """
    str_list = str.split(' ')
    if len(pattern) != len(str_list):
        return False
    char2string = {}
    string2char = {}
    i = 0
    while i < len(pattern):
        char = pattern[i]
        string = str_list[i]
        if (char in char2string and string != char2string[char]) or (
                string in string2char and char != string2char[string]):
            return False
        char2string.setdefault(char, string)
        string2char.setdefault(string, char)
        i += 1

    return True
if __name__ == '__main__':
    print(wordPattern('abba','dog cat cat dog'))