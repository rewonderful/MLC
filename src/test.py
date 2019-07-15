#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def generateParenthesis( n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []
    if n == 0:
        return ans

    def dfs(left, right, path):
        if left + right == 2 * n:
            ans.append(path)
        if left < n:
            dfs(left + 1, right, path + '(')
        if right < n and right < left:
            dfs(left, right + 1, path + ')')

    dfs(0, 0, '')
    return ans
if __name__ == '__main__':
    print(generateParenthesis(3))