#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def chinese(data):
    count = 0
    for s in data:
        if ord(s) > 127:
            count += 1
    return count
if __name__ == '__main__':
    s = input('please input')
    for i in range(1, len(s)):
        s_list = list(s)
        s_list.insert(i, " ")
        print(''.join(s_list))
   #  a = ListNode(1)
   #  b = ListNode(1)
   #  c = eval('isinstance(a, ListNode)')
   #  print(c)
   #  print(id(a) == id(b))
   #
   #  a.next = 3
   #
   #  print(b.next)
   #
   #
   #  print(isinstance(a, ListNode))
   #
   # # print(id(a) == id(b))
   # print("{0:>20}".format('ab'))
   # print("{0:>20}".format('aaabbb'))
   # print("%20s"%('中文'))
   # print(' '*8+'长一点的中文')
   # print("%20s"%('长一点的中文'))
   # zw = '中文'
   # number = chinese('中文')
   # print('{0:>{wd}}'.format(zw,wd=20-number))
   # lzw = '长一点的中文'
   # number = chinese(lzw)
   # print('{0:>{wd}}'.format(lzw, wd=20 - number))

   # print('{0:{1}>20}'.format('中文', chr(12288)))  # 居中对齐
   # print('{0:{1}>20}'.format('长一点的中文', chr(12288)))  # 居中对齐



