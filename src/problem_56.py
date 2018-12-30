#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def merge(self, intervals):
    """
    算法：先排序，再merge
    MD,坑爹，interval居然是个对象，而不是题目中给出的样例那样的[1,2][3,4]🙄🙄🙄🙄🙄
    然后就很好做了，根据interval.start进行排序，然后result的top做判断是否要进行合并，合并的条件是
    interval.left <= last_interval.end，因为已经根据start排过序了，所以只要判断这一个地方就oK

    """
    if intervals == []:
        return []
    intervals.sort(key=lambda x: x.start)
    result = []
    for interval in intervals:
        if result == []:
            result.append(interval)
            continue
        else:
            last_interval = result[-1]
            if interval.start <= last_interval.end:
                interval.start = min(interval.start, last_interval.start)
                interval.end = max(interval.end, last_interval.end)
                result.pop()
            result.append(interval)
    return result

def merge1(self, intervals):
    """

    Solution的写法，更加简洁
    """
    intervals.sort(key=lambda x: x.start)

    merged = []
    for interval in intervals:
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.
        if not merged or merged[-1].end < interval.start:
            merged.append(interval)
        else:
        # otherwise, there is overlap, so we merge the current and previous
        # intervals.
            merged[-1].end = max(merged[-1].end, interval.end)

    return merged
if __name__ == '__main__':
    print(merge([[1,4],[4,5]]))