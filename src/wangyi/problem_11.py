#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import itertools
def groupby(pairs):
    help_dict = dict()
    for p in pairs:
        key = (p[0],p[2])
        if key not in help_dict:
            help_dict[key] = [p]
        else:
            help_dict[key].append(p)
    return help_dict



def solution(n,pairs):
    inner_product =[[a[0]]+[a[1]]+[b[0]]+[b[1]] for a in pairs for b in pairs]
    do_where = []
    for pair in inner_product:
        if pair[1] == pair[3] and pair[0] != pair[2]:
            do_where.append(pair)
    after_groupby = groupby(do_where)
    ans = []
    for k,v in after_groupby.items():

        ausernames = set()
        for p in v:
            ausername = p[1]
            ausernames.add(ausername)
        num = len(ausernames)
        if num > 2:
            ans.append([*k,str(num)])
    ans.sort(key=lambda x:(x[0],x[1]))

    return ans


if __name__ == '__main__':
    n = int(input().strip())
    pairs = []
    for _ in range(n):
        pairs.append(tuple(input().strip().split(" ")))

    #tmp = ["ddd Kate", "ccc Kate","ccc Beal","eee Tom","ddd Beal","bbb Kate","ddd Tom","ccc Tom",]

    ans = solution(n,pairs)
    for s in ans:
        print(" ".join(s))