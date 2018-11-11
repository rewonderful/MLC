#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#杨辉三角
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    result = []
    for i in range(numRows):
        inner_list = []
        for j in range(i+1):
            if j ==0 or j == i:
                inner_list.append(1)
            else:
                inner_list.append(result[i-1][j-1]+result[i-1][j])
        result.append(inner_list)
    return result


if __name__ == '__main__':
    numRows = 3
    print(generate(numRows))