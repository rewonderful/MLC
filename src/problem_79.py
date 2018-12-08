#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def minWindow( s, t):
    """
    算法：移动窗口+哈希表
    思路：
        用移动窗口来容纳子串，然后关键在于思考如何根据当前情况更新窗口的起止位置，即更新子串情况

        用begin，i维护一个窗口W，窗口W内记录包含所有T内字符的子串
            begin记录子串起始位置，i 用来扩展窗口的边界，记录子串末尾
        用两张哈希表来构成子串与要求的条件，map_t记录模式t要求的字符的数量，char_in_window来记录当前
        窗口W内各字符的数量
            算法如下：
                1. 初始化map_t，得到要求的模式
                2. 挪动窗口尾部i，使begin和i之间的窗口构成的子串符合要求的模式
                3. 当窗口W内的子串已经符合map_t要求的模式时，就考虑将begin右移
                    a).这里符合模式用一个单独的函数判断若map_t中要求的字符在char_in_window中都有
                       且在char_in_window中的数量>=map_t中的数量的话，才是符合模式的，否则不符合
                    b).本题中，可以右移的条件有两个
                        1). 当前begin所指的字符不是map_t中要求的字符，则可以右移一位（其实想一想，最
                            短的符合模式的子串，左右端点一定是要求的模式中的字符）
                        2). 当前begin所指的字符虽然是map_t中要求的字符，但是当前窗口W中记录的该字符char
                            的数量count 是大于map_t[char]模式要求中的数量的，意味着后面还有这个字符，当前
                            字符可以跳过，故右移
                    否则当当前字符在map_t中且数量刚好等于map_t[char]模式所要求的数量时，不能跳过，break
                4. 更新最短符合条件的子串长度及子串值
    复杂度分析：
        时间：ONk，虽然只是用i遍历了一次字符串，但我觉着是ONK，因为is_window_ok要遍历k个模式中要求的字符，且
                  还要移动begin的位置，但是看题解的意思这应该也属于ON的解法？懵逼= =🤔🤔
        空间：ON，两个哈希表
    """

    min_window = ''
    if s == '' or t == '':
        return min_window
    begin = i = 0
    min_len = float('inf')
    char_in_window = {}
    map_t = {}
    for char in t:
        map_t.setdefault(char, 0)
        map_t[char] += 1

    def is_window_ok(map_t, map_window):
        for k, v in map_t.items():
            if k not in map_window or map_window[k] < v:
                return False
        return True

    while i < len(s):
        if s[i] in map_t:
            char_in_window.setdefault(s[i], 0)
            char_in_window[s[i]] += 1
        if is_window_ok(map_t, char_in_window):
            while begin < i:
                if s[begin] not in map_t:
                    begin += 1
                elif char_in_window[s[begin]] > map_t[s[begin]]:
                    char_in_window[s[begin]] -= 1
                    begin += 1
                else:
                    break
            if i - begin + 1 < min_len:
                min_len = i - begin + 1
                min_window = s[begin:i + 1]
        i += 1
    return min_window



if __name__ == '__main__':
    print(minWindow("AA","AA"))