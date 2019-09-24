#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def conv2k(num, k):


    conv = list(range(10)) + list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    index = []
    while True:
        yushu = num % k
        shang = num // k
        index += [yushu]
        if shang == 0:
            break
        num = shang
    index.reverse()

    return ''.join([str(conv[i]) for i in index])

def solution(num1, num2, k,syb):
    num1,num2 = int(num1,k),int(num2,k)
    if syb == "+":
        return conv2k(num1 + num2,k)
    elif syb == "-":
        return conv2k(num1 - num2,k)
    elif syb == "*":
        return conv2k(num1 * num2,k)


if __name__ == '__main__':
    T = int(input().strip())
    nums = []
    symbols = []
    for _ in range(T):
        k = int(input().strip())
        num1, num2, syb = input().strip().split()
        nums.append((num1,num2))
        symbols.append(syb)
        print(solution(num1,num2,k,syb))
