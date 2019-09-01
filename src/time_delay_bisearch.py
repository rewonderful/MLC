#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def search(time_split,target):

    for i in range(len(time_split)):
        element = time_split[i]
        if element == target:
            return i
        elif element > target:
            return i
    return len(time_split)
if __name__ == '__main__':
    target = 77
    time_split = [0,10,36,50,80]
    print(search(time_split,target))