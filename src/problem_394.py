#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def decodeString(self, s):
    """
    My Method
    算法：栈
    思路：
        在栈内保持字符串，和重复的数字
            检测到数字的话，向后一直检测，把完整的数字存下来，压栈

            检测到字母的话，向后一直检测，把连续的完整的字符串存下来，压栈

            然后遇到']'的时候，处理栈内的元素
            栈顶一定是字符串，因为数字后一定会跟字符串，所以栈顶不可能是数字。然后pop出栈顶，看看栈顶前面
        有没有元素，有的话判断是字符串还是数字，如果是数字的话，就弹出，进行repeat操作，然后再判断此时的栈顶，
        如果栈不为空且不是字符串，那么就将二者拼接，类似于2[a3[b]]时bbb构建好了，要和a拼接，形成abbb，然后再
        将abbb入栈，这样看像一个递归的过程
            然后由于原pattern可能会有尾部的字符串即2[a3[b]]leetcode，所以将尾部特殊处理，也就是检测到最后一个
        连续的字符串的时候，存在self.tail里面，最后拼进stack构造的字符串中
            因为检索的过程中不一定能将所有字符串都构造好，也就是i达到长度len(s)的时候stack内还没有被处理成只剩下
        一个元素，所以再接一个while将栈内元素从栈顶开始按照上面的方式去处理，出栈，repeat，连接前序字符串

            最后返回的就是stack[-1]+self.tail
    """
    stack = []
    i = 0
    self.tail = ''
    while i < len(s):
        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            stack.append(s[i:j])
            i = j + 1 #因为此时s[j]一定是 [，所以 i = j+ 1
        elif s[i] == ']':
            tmp_str = stack.pop()
            if stack != [] and stack[-1].isdigit():
                repeat = stack.pop()
                tmp_str = tmp_str * int(repeat)
            if stack != [] and not stack[-1].isdigit():
                tmp_str = stack.pop() + tmp_str
            stack.append(tmp_str)
            i = i + 1
        else:
            j = i
            while j < len(s) and not s[j].isdigit() and not s[j] in ('[', ']'):
                j += 1
            if j < len(s):
                stack.append(s[i:j])
            else:
                self.tail = s[i:j]
            i = j
    while len(stack) > 1:
        tmp_str = stack.pop()
        if stack != [] and stack[-1].isdigit():
            repeat = stack.pop()
            tmp_str = tmp_str * int(repeat)
        if stack != [] and not stack[-1].isdigit():
            tmp_str = stack.pop() + tmp_str
        stack.append(tmp_str)
    return stack[-1] + self.tail if len(stack) > 0 else self.tail
if __name__ == '__main__':
    print(decodeString("leetcode"))