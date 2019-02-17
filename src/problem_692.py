#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import collections,heapq


def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
    """

    建立堆来保持TOP N的次序
    key就是 - freq 和word
    然后pop k次的元素就是要求的TOP K

    """
    counter = collections.Counter(words)

    heap = [(-freq, word) for word, freq in counter.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]
def topKFrequent1(self, words: 'List[str]', k: 'int') -> 'List[str]':
    """

    算法：排序
    思路:
        统计词频后进行排序，用sort，key就是-counter[word]和 word
    """
    counter = collections.Counter(words)
    candidates = list(counter.keys())
    candidates.sort(key=lambda word: (-counter[word], word))

    return candidates[:k]