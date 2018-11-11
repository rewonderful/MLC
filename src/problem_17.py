#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    import itertools
    letter_dict ={}
    letter_dict['2'] = ['a','b','c']
    letter_dict['3'] = ['d','e','f']
    letter_dict['4'] = ['g','h','i']
    letter_dict['5'] = ['j','k','l']
    letter_dict['6'] = ['m','n','o']
    letter_dict['7'] = ['p','q','r','s']
    letter_dict['8'] = ['t','u','v']
    letter_dict['9'] = ['w','x','y','z']
    ans = []
    if len(digits) > 0:
        ans = letter_dict[digits[0]]
    else:
        return ans

    for i in range(1,len(digits)):
        new_letter = letter_dict[digits[i]]
        ans = [(char+nl) for char in ans for nl in new_letter ]
    return ans
def letterCombinations_recursion(digits):
    letter_dict = {}
    letter_dict['2'] = ['a', 'b', 'c']
    letter_dict['3'] = ['d', 'e', 'f']
    letter_dict['4'] = ['g', 'h', 'i']
    letter_dict['5'] = ['j', 'k', 'l']
    letter_dict['6'] = ['m', 'n', 'o']
    letter_dict['7'] = ['p', 'q', 'r', 's']
    letter_dict['8'] = ['t', 'u', 'v']
    letter_dict['9'] = ['w', 'x', 'y', 'z']
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return letter_dict[digits[0]]

    behind = letterCombinations_recursion(digits[1:])
    return [x+y for x in letter_dict[digits[0]] for y in behind]


if __name__ == '__main__':
    digits = '222'
    #print(letterCombinations(digits))
    print(letterCombinations_recursion(digits))