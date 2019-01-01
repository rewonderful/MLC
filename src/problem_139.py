#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def wordBreak(self, s, wordDict):
    """
    算法：动规
    思路：
        首先要联想到动规上去，再建立状态转移方程
        因为leetcode这样的单词，如果code是在wordDict中的，那么再看前面的leet是不是一个True的状态就可以确定
        leetcode是一个True的单词，可以构成i与i-1的关系，并且可以自底向上解决问题
            状态转移方程其实也是根据上面这个思想去建立的
            当前状态dp[i]存储从0到第i个位置的子串是否满足题目的要求
            在第i个位置，向前数，数到一个word in wordDcit后，dp[i] = dp[j]，存的时候要dp[i+1]是因为
            dp和s的长度不一样，len(dp) = len(s)+1,
            边界条件dp[0] = True，比如leet这个单词,dp[4] = dp[0],dp[0]应该是True的

    """
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(len(s)):
        j = i
        while j >= 0:
            if s[j:i + 1] in wordDict and dp[j]:
                dp[i + 1] = True
                break
            j -= 1
    return dp[-1]

def wordBreak1( s, wordDict):
    """
    算法：动规
    思路：
        和上面方法的思路是一样的，不过这里用的是下一层直接遍历wordDict而不是再用j开始数
        对wordDict中的每一个w进行尝试，如果当前位置向前能拼接成word的话，就看看当前位置前的dp存储的是True还是False
        条件中有or i-len(w) == -1 是为了加上"边界条件"，即一个词是leet这样的，i-len(w) == -1，也应该是True

    """
    d = [False] * len(s)
    for i in range(len(s)):
        for w in wordDict:
            if w == s[i - len(w) + 1:i + 1] and (d[i - len(w)] or i - len(w) == -1):
                d[i] = True
    return d[-1]
if __name__ == '__main__':
    print(wordBreak("leetcode",["leet","code"]))

