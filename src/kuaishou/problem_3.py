#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def solution(order,n):
    if order == []:
        return order

    v_list = []
    p_list = []
    p2i= {}
    v2i = {}
    for i in range(len(order)):
        if order[i][0] == 'V':
            v_list.append(order[i])
            v2i[order[i]] = i
        else:
            p_list.append(order[i])
            p2i[order[i]] = i
    result = []
    i = 0
    has_p = False
    while i < len(order):
        item = order[i]
        if  len(result) > 0 and (len(result)) % n == 0:
            has_p = False
        if item[0] == 'V':
            if len(p_list) > 0 and p2i[p_list[0]] < v2i[item] and not has_p:
                result.append(p_list.pop(0))
                has_p = True
                continue
            else:
                result.append(item)
        elif not has_p and len(p_list) > 0 :
            result.append(p_list.pop(0))
            has_p = True
        i += 1
    i = len(result) % n
    return result

if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())
    order = []
    for _ in range(M):
        order.append(input().strip())
    #order = "V_0,V_1,V_2,P_3,P_4,P_5,V_6,P_7,V_8,V_9"
    #order = order.split(',')
    #print(solution(order,N))
    result = solution(order,N)
    print(len(result))
    for item in result:
        print(item)