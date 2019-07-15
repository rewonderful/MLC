#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        if n == 0:
            return self.ans
        def dfs(left,right,path):
            if left == 0 and right == 0:
                self.ans.append(path)
            if left >0:
                dfs(left-1,right,path+'(')
            if right > 0 and right > left:
                dfs(left,right-1,path+')')
        dfs(n,n,'')
        return self.ans

def generateParenthesis(self, n):
    """
    问题分析：
        1. n对括号有2n个字符，每个字符有两种可能性出现，'('或者')'，字符串生成就可以看成递归问题，当前i字符填充后，
        剩余n-i个生成，把他们拼接在一起，就是生成的括号对，有点像i + [i:]的感觉

        2. 可以暴力生成所有可能的组合，然后挑选出valid括号对
        3. 怎样的括号对是valid？左括号一定有右括号匹配，进一步看，在生成的每一步过程中，左括号出现的次数一定大于右括号次数
        当左右括号数相加==2n时，整个括号对生成完成
    关键：
        1. 在生成的过程中，就去判断是不是一个valid对，即，只向ans[]数组中添加valid的括号对，避免暴力枚举所有可能再筛选
        2. 生成过程中，字符串长度==2n且生成过程中的每一步，right都<=left，亦即right<left时right才添加，否则不添加，这样生成的字符串一定是valid
    算法：
        1. 回溯
        2. "停止条件"：当左右括号都用完了， left+right==2n时应该添加到ans中
        3. 每一次递归生成时，记录左右括号数，左右括号各n个，先放左括号，因为右括号能不能放取决与当前字符串中左括号的情况
        4. left<n时，才添加左括号，right<left时，才可以添加右括号，添加后把状态（即添加字符后的字符串）传入下一个递归中，left和right的计数值+1
    复杂度分析：
        时间：O（4n/sqrt(n)）copy 题解， Each valid sequence has at most n steps during the backtracking procedure.
        空间：O（4n/sqrt(n)）copy 题解， as described above, and using O(n)O(n) space to store the sequence.
    """
    ans = []

    def backtracking(parenth, left, right):
        if left + right == 2 * n:
            ans.append(parenth)
        if left < n:
            backtracking(parenth + '(', left + 1, right)
        if right < left:
            backtracking(parenth + ')', left, right + 1)

    backtracking('', 0, 0)
    return ans

def generateParenthesis1( n):
    """
        My method
    """

    def generate(left, right, path, result):
        if left + right == 2*n:
            result.append(path)
            return
        if left < n:
            generate(left + 1, right, path + '(', result)
        if right < left:
            generate(left, right + 1, path + ')', result)

    result = []
    generate(0, 0, '', result)
    return result
if __name__ == '__main__':
    print(generateParenthesis1(3))