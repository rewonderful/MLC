#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def get_disstance(s1,s2):
    s1 = set(s1)
    s2 = set(s2)
    jaccard  = len(s1 & s2) / len(s1 | s2)
    return jaccard
def solution(s1,s2):
    result = []
    


    pass

if __name__ == '__main__':
    #s1 = "床前明月光,疑是地上霜,举头望明月,低头思故乡".split(',')
    #s2 = "越光".split(',')
    s1 = input().strip().split(',')
    s2 = input().strip().split(',')
    x = int(input())
    print(solution(s1,s2))
