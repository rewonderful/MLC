#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def singleNumber(self, nums):
    """
    如果是出现两次的话，用一个bit就可以
    比如 b，初始为0
    当5第1次出现时， b=5
    当5第2次出现是， b清空为0，表示b可以去处理其他数字了
    所以，最后 如果 b !=0的话，b记录的就是只出现了一次的那个数字

    ->公式就是 b = b xor i  或者 b = b^i


    那么，如果是三次的话，香浓定理，需要用2bits进行记录

    当5第一次出现的时候，b = 5, a=0,  b记录这个数字
    当5第二次出现的时候，b = 0, a=5， a记录了这个数字
    当5第三次出现的时候，b = 0, a=0， 都清空了，可以去处理其他数字了
    所以，如果有某个数字出现了1次，就存在b中，出现了两次，就存在a中，所以返回 a|b

    公式方面 ，上面两次的时候，b清空的公式是 b = b xor i
            而第三次时，b要等于零，而这时a是True，所以再 & 一个a的非就可以，b = b xor & ~a
    -> b = b xor i & ~ a
       a = a xor i & ~b
    """
    a = b = 0
    for num in nums:
        b = b ^ num & ~a
        a = a ^ num & ~b
    return a | b

def singleNumber1(self, nums):
    """
        三进制不进位加法，比如02 + 01 = 00 (2+1=3做加法不进位)。所以同一个数，比如7的三进制表示为21，21+21+21 = 00 即
    十进制下的0。最终代码即统计每一位上1，对3取模
    ----------------------------------------------------------------------------------------------------------------
        用3个整数来表示INT的各位的出现次数情况，one表示出现了1次，two表示出现了2次。当出现3次的时候该位清零。最后答案就是one的值。

        ones   代表第ith 位只出现一次的掩码变量
        twos  代表第ith 位只出现两次次的掩码变量
        threes  代表第ith 位只出现三次的掩码变量
        假设现在有一个数字1，那么我们更新one的方法就是‘亦或’这个1，则one就变成了1，而two的更新方法是用上一个状态下的one去‘与’上数
    字1，然后‘或’上这个结果，这样假如之前one是1，那么此时two也会变成1，这make sense，因为说明是当前位遇到两个1了；反之如果之前one
    是0，那么现在two也就是0。注意更新的顺序是先更新two，再更新one，不理解的话只要带个只有一个数字1的输入数组看一下就不难理解了。然后
    我们更新three，如果此时one和two都是1了，那么由于我们先更新的two，再更新的one，two为1，说明此时至少有两个数字1了，而此时one为1，
    说明了此时已经有了三个数字1，这块要仔细想清楚，因为one是要‘亦或’一个1的，值能为1，说明之前one为0，实际情况是，当第二个1来的时候，
    two先更新为1，此时one再更新为0，下面three就是0了，那么‘与’上three的相反数1不会改变one和two的值；那么当第三个1来的时候，two还
    是1，此时one就更新为1了，那么three就更新为1了，此时就要清空one和two了，让它们‘与’上three的相反数0即可，最终结果将会保存在one中
    """
    ones, twos, threes = 0, 0, 0
    for item in nums:
        twos |= ones & item
        ones ^= item
        threes = ones & twos

        ones ^= threes
        twos ^= threes
    return ones
def singleNumber2(self, nums):
    """
    算法：哈希表
    思路：
        统计一下，统计值==1的加入答案
    复杂度分析：
        时间：ON，
        空间：ON
    """
    record = {}

    for num in nums:
        record.setdefault(num, 0)
        record[num] += 1
    for k, v in record.items():
        if v == 1:
            return k