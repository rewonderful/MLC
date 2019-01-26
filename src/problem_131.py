#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def partition(self, s):
    """
    算法：递归
    其实就是依次拆解这个字符串
    从头开始，相当于是贪婪地拆，拆下来一个回文子串后，剩下的字符串继续拆回文子串，直到所有字符都拆完了，
    然后将答案添加到result中
    判断回文的方法就是s = s[::-1]
    然后要注意s[:i]是不包含第i位的，所以向下传的时候，传s[i:]就好了
    以及range的始末位置是1和len(s)+1，从0开始的话会取到空串，最后补len(s)+1的话，会无法取到整个字符串
    """
    self.result = []

    def dfs(s, path):
        if s == '':
            self.result.append(path)
            return
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                dfs(s[i:], path + [s[:i]])

    dfs(s, [])
    return self.result