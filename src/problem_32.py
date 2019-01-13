#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def longestValidParentheses(self, s):
    """
    Solution Method
    算法：动规
    思路：
            我一开始想的是和最长回文子串一样，用一个二维数组dp[i][j]来记录到s[i:j+1]部分是不是valid括号
        就像回文子串一样用动规数组记录valid情况，而不是直接记录最长的子串长。这样的话还是要ON2K，ON2是因为
        要两层for，k是因为，在判断诸如"(()())"这样的情况时，我需要一个变量k去遍历这个substring判断会不会
        在某个位置k使得dp[i][k]和dp[k+1][j] 都是True，如果有的话就说明dp[i][j] == T，这样时间复杂度还是
        没有下来
            题解的这种解法也算是比较巧妙了，直接用一维数组记录第i个位置结尾的最长子串的长度
            显然只有第i个位置是")"的时候，才可能在该位置形成合法串，然后先看i-1，如果i-1是'('的话，那么显然
        dp[i] = dp[i-2]+2，就是在前面的基础上再加2这样
            否则如果i-1的字符也是')'的话，就应该根据dp[i-1]找到前一个位置形成子串的最长的左侧的那个'('，
        这个位置是i-dp[i-1]，前一个字符就是k = i-dp[i-1]-1，如果k是'('的话，那么如果dp[i] = dp[i-1]+2+before
        before就是dp[k-1]的情况，把前面的加起来补上
    """
    if len(s) < 2:
        return 0
    ans = 0
    dp = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            elif s[i - 1] == ')' and i - dp[i - 1] > 0:
                k = i - dp[i - 1] - 1
                if s[k] == '(':
                    before = dp[k - 1] if k >= 2 else 0
                    dp[i] = dp[i - 1] + 2 + before
        ans = max(ans, dp[i])

    return ans


def longestValidParentheses1( s):
    """
    Solution method 2
    算法：栈
    思路：
        用栈来维护合法的括号对位置，在匹配的过程中就记录下来最长的括号对
        匹配的过程就和普通的验证一样，左括号入栈，右括号来的时候出栈，匹配
        这里栈内的栈顶表示的是【当前合法左括号的起始位置】！所以栈内存的是下标
            在遍历过程中，用i-top，即i-stack[-1]来计算合法的括号长度，0,1,1-0要+1才等于2，
        所以先在栈内存一个数字-1，保障当出现()这样的括号时，是能根据栈顶stack[-1] = -1 计算出长度1-(-1) = 2
            然后还是左括号入栈，右括号来了，如果栈不空，出栈，计算长度，如果栈空的话，将右括号的位置入栈，此时
        就相当于是记录下了合法左括号前的那个位置，就像上面提到的0，1，0前面的-1一样，从而保障能用i-stack[-1]
        获得当前最长的子串的起始位置，然后一减就是长度
            多想想这个例子就通了"()((()))",'()))()()'

        """
    if len(s) < 2:
        return 0
    stack = [-1]
    ans = count = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            count = i - stack[-1]
            if count > ans:
                ans = count
    return ans
if __name__ == '__main__':
    print(longestValidParentheses1("()((()))"))