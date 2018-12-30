#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def sortColors( nums):
    """
    算法：类似三路快排的多指针法
    思路：
        其实比较容易联想到用类似于三路快排的做法，其实只看题意的话也应该联想到用类似于快排的做法
        因为就是对0，1，2进行排序嘛，
        0，1，2以1做为pivot分割的话正好就是小于1的是一撮，大于1的是一撮，也就是0，1，2的排序
        那么就可以借用三路快排的思路来做
        注意red,white,blue分别对应于0,1,2
        设置red_end,i,blue_start分别表示如下含义：
            red:[0,red_end)
            white[red_end,i)
            blue:[blue_start+1,end]
        red_end记录最后一个红色的后一个位置，i记录最后一个white的后一个位置，blue_start记录blue开始的前一个位置

        初始设red_end,i=0，blue_start = len -1 ，注意，因为是这样设置的初始条件，所以当检测到一个2，即blue时，
        对将blue_start的位置与i对调后只将blue_start -= 1，i不后挪，因为调换过来的值还不能确定就要放在i这里，所以
        下一次循环时会挪动他，这里的感觉就像是快排如果选nums[lo]=pivot时，就要先从右边hi的位置开始判断是一样的

        反正大体思路就是，发现一个blue，根据blue_start去调换位置，放在blue区域，发现一个white，i+=1，不用管
        发现一个red，调换，然后red_end+=1,i+=1

        [0...red_end,white_white_white,blue_start....end]

    """
    red_end, i, blue_start = 0, 0, len(nums) - 1
    while i <= blue_start:
        if nums[i] == 1:
            i += 1
        elif nums[i] == 2:
            nums[i], nums[blue_start] = nums[blue_start], nums[i]
            blue_start -= 1
        else:
            nums[i], nums[red_end] = nums[red_end], nums[i]
            red_end += 1
            i += 1

if __name__ == '__main__':
    print(sortColors([2,0,2,1,1,0]))