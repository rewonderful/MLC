#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def longestPalindrome2( s: str) -> str:
    if s == "":
        return s
    ans = s[0]
    n = len(s)
    dp = [[i == j for i in range(n)] for j in range(n)]
    for i in range(1, n):
        if s[i] == s[i - 1]:
            dp[i - 1][i] = True
            ans = s[i - 1:i + 1]
    for j in range(len(s)):
        for i in range(j - 1):
            dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
            if dp[i][j] and j - i + 1 > len(ans):
                ans = s[i:j + 1]
    return ans
def longestPalindrome(self, s):
    """
    算法：动态规划DP
    思路：
        本题中的动规其实是对暴力解法的一种优化，所以还是，先思考暴力解法怎么做？
        暴力解法：
            遍历所有的可能的字符串，for ... for ... 两层 ，然后依次判断每个字符串是否是回文串，s==s[::-1]，逆序ON
        所以暴力解法的时间复杂度是ON3
        动规：
            动规就是在暴力解法的基础上，优化了判断子串是否为回文串这一步。判断某个位置i,j是不是回文串，可以先看看(i+1,j-1)
        是不是回文串并且是否s[i]==s[j]，故用dp存储s(i,j)是否为回文串，如此便可以建立起状态转移方程：
            dp[i][j]= dp[i+1][j-1] and s[i]==s[j]
            边界条件:
                dp[i][i] = True
                dp[i][i+1] = s[i]==s[i+1]
            如此一来便可以在暴力解法的基础上进行优化改进，将时间复杂度进一步压缩
        ❗️❗️❗️：
            要注意实现的时候，两层for的顺序！
            譬如以下代码中的后半部分，我原来写的是
            for i in range(len(s)):
                for j in range(i+1,len(s)):
                    #CODE
            这样写是一个很符合常规思路的想法，就是遍历所有的子串嘛，但是！一定要记得！动规的题，dp的状态是什么是很有讲究的！
        因为状态转移方程要和子状态建立起关系，所以要考虑我们这里的dp存的是什么。以及这个状态转移的【路径】是否正确！就像
        二维矩阵机器人往右下角最少走几步的那种题一样，机器人是可以向右向下走的，所以看一下这里的【路径】是什么
            拿一个上面这种for跑错的结果为示例
            case:"abcba"，answer:"bcb"
            为什么错了？为什么不是"abcba"?
            可以看到，当i==0,j== 4时 dp[0][4] = dp[1][3] and s[0] == s[4]，而遍历到0,4时，1，3还没有遍历！也就是说我依赖的子
        状态还没有求解！所以会导致错误的答案！
            那么联想其他一些题的dp做法，比如一个一维数组的最大子序列和，dp存的是子序列最后一位是当前i的最大子序列和！，所以这里也是
        一样的，dp是存i,j是否为回文串没错，但是遍历顺序是以j为结尾的子串是否为回文串！所以改写for循环为
            for j in range(len(s)):
                for i in range(j - 1):
                    #CODE
            这样case="abcba"时，j=4,i=0，代表的是以s[4]结尾的子串是否为回文串，这个时候再去找s[1][3]的时候，已经建立了s[1][3]的值！
        ✨✨✨：
            这种感觉就像是，反正都是两层for 都能把所有的子串都遍历，生成一遍，但是两层for的遍历方式也有很多，要选择一种和动态规划
        状态转移方式，能正确地将子状态和当前状态保证先后顺序连接起来的那种遍历方式！
    复杂度分析：
        时间：ON2,显然
        空间：ON2,dp数组空间
    """
    if s == '':
        return s
    ans = s[0]
    dp = [[i == j for j in range(len(s))] for i in range(len(s))]
    for i in range(len(s) - 1):
        dp[i][i + 1] = s[i] == s[i + 1]
        if dp[i][i + 1] and len(ans) < 2:
            ans = s[i:i + 2]
    for j in range(len(s)):
        for i in range(j - 1):
            dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
            ans = s[i:j + 1] if dp[i][j] and len(s[i:j + 1]) > len(ans) else ans
    return ans

def longestPalindrome1(self, s):
    """
    算法：从中间扩散
    思路：
        换个角度看回文串，将回文串看做是从中间向两边扩展的，
        比如，
            'abcba'就可以看做是从c扩展，左右都是b，左右都是a，
            'abba'，可以看做中间是bb，左右都是a
        所以对每一个位置i取尝试左右最大能扩展到多少，
            要注意要扩展两次：
                一次找奇数长度的回文序列：中间位置i,i
                一次找偶数长度的回文序列：中间位置i,i+1
            helper中return的是s(l:r)而不是s[l:r]，因为向外拓展的时候左右会扩，扩到跳出while循环后，说明是不满足while
        的条件的(即当前是回文，可以扩展的条件)，说明上一个状态是满足【合法且是回文的】，所以要返回上一个状态即s(l:r)-->s[l+1,r]
    复杂度分析：
        时间：ON2，显然
        空间：O1，常数级
    """
    res = ""

    def helper(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    for i in range(len(s)):
        #扩展奇数长度
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        #扩展偶数长度
        tmp = helper(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res
if __name__ == '__main__':
    s="abcba"
    print(longestPalindrome2(s))