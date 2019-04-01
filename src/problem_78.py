#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def subsets0( nums):
    """
    算法：递归/回溯
    思路：
            从数学意义上看，生成一个含n个元素集合的子集，共有2^n个，组成的方法就是每个元素都有添加和
        不添加两种，同理，根据该思路来解此题。
            直接写for循环的话如果第一层用i in range(len(nums))，那么第二层也用i in range(len(nums))
        只能生成含两个元素的子集，也就是几层for循环生成含几层元素的子集，譬如，[1,2],[1,3],[2,3]，况且
        这样还不好去重。而利用递归的特点就非常好控制了，因为递归的深度可以是不定的，不像for循环套几层往往
        是写定的。
            回头再看我们人手动生成子集的过程：子集内某个元素nums[i]都有加入和不加入该子集两种选择，那么
        可以将判断的过程看做是一颗二叉树，节点代表的是当前子集的构成情况，根节点为[]，从第1层开始，或者说
        i+1层中就是对第i个元素nums[i]进行判定，判断nums[i]这个元素是否加入当前的子集，如果加入就会形成一个
        新的子集，不加入的话，当前子集和父节点的子集情况是一样的（因为没加入当前节点嘛）。根据该思路以及
        树的特点。便可以比较容易地想到递归式子的写法
            据此就很好写递归式子了，传入nums，以及当前判断的是第几个元素i，这样就可以nums[i]来取当前元素，
        当前集合状态subset，以及将结果带出去的变量result
        注意：
            1、一般来说递归都有终止条件，满足终止条件时一定return，不管这时的return是否会将当前结果传
            给上一层但是一定会return来终止，不然的会无限循环。此外在终止条件的"else"部分，不一定非要有
            return，return的意义要么是终止递归，要么是将结果返还，但是就本题中，完全可以传入一个result
            来贯穿整个递归的过程
            2、千万小心Python的深拷贝和浅拷贝以及对可变对象传递的值是引用，也就是传入列表的话，如果不传入
            列表的拷贝，传入的就是引用，函数内改变列表会影响函数外列表的值，这里result我们希望传入的是
            引用，但是每一层的子集状态subset我们希望传入的是它的值，是拷贝，这样才能在不同节点就不同状态
            的子集，而不是每一时刻的子集都指向内存中的同一个列表对象，这样各个位置改变的都是同一个列表
            最终无法得到我们要的各不同的子集状态

    复杂度分析：
        时间：O2^N，遍历所有O2^N个子集（也是O2^N种可能的情况）
        空间：O2^N，递归栈空间以及存储子集的result的空间
    """

    def generate(i, nums, subset, result):
        if i >= len(nums):
            return
        #当前元素不添加
        generate(i + 1, nums, subset[:], result)
        #当前元素添加
        subset.append(nums[i])
        result.append(subset[:])
        generate(i + 1, nums, subset[:], result)
    result = [[]]
    generate(0, nums, [], result)

    return result

def subsets_new(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    self.ans = [[]]
    self.set = {}

    def dfs(i, subset):
        subset.append(nums[i])
        if tuple(subset) not in self.set:
            self.ans.append(subset)
        for j in range(i + 1, len(nums)):
            dfs(j, subset[:])

    for i in range(len(nums)):
        dfs(i, [])

    return self.ans
def subsets1(self, nums):
    """
    算法：位运算
    思路：
            n个元素的集合，有2^n次方个子集，每个元素都有出现和不出现两种可能，很自然地可以联想到二进制
        表示，000代表空子集,001代表只有第三个位置有元素的子集,011代表只有后两个元素的子集。如此一来
        可以将原问题构造成二进制的问题，比如集合有3个元素ABC，可以求出来所有子集的表达二进制表达方式（事实
        上不用取求，只要用位运算符，就自然而然地将子集用二进制表示了）。可以将ABC分别表示为100,010,001或者
        001,010,100,表示的顺序不关键，重点是每个元素由互斥的one-hot形式构成即可。
            位运算&是逐位运算，构造one-hot形式的元素表示后，如100，与子集101做按位与运算即，100&101 = 101 = 5 >0
        只要当one-hot位置的1在子集的二进制中也有1，就代表这个元素在这个子集中，那么运算结果一定>0，由于one-hot除了
        1位是1其他位都是0，所以这样构造后可以通过按位与&的结果是否大于0判断该元素是否在该子集中

            其实这种解法的思路应该理解为，我已经构造出了所有的子集，2^n次个，只不过我现在拿nums把它翻译过来罢了
        So：
            1. 生成所有子集的二进制表示（只要生成所有子集的十进制形式然后后面用位运算的时候就会"转为"用二进制了）
            2. 对每一个子集的二进制形式：
                遍历nums中将one-hot编码后的元素与当前子集按位与，判断该元素是否在该子集中，在的话就subset.append
                完成"翻译"
                这里one-hot的编码顺序可以从高到低(1<<(len(nums)-1-j))也可以从低到高(1<<j)
                    从低到高：[A,B,C]->[0,1,2]->[001,010,100]
                    从高到低：[A,B,C]->[0,1,2]->[100,010,001]
    复杂度分析：
        时间：NO2^N，第一层forO2^N，第二层ON
        空间：O2^N，result，O2^N，subset，ON的空间
    """
    all_set = 1<<len(nums)
    result = []
    for i in range(all_set):
        subset = []
        for j in range(len(nums)):
            #或者1<<(len(nums)-1-j) & i
            if 1<<j & i :
                subset.append(nums[j])
        result.append(subset)
    return result
def subsets2( nums):
    """
    算法：循环/迭代
    思路：
        类似于我们人手写生成集合的方式，逐个元素的添加到已有的结果里，并且对已有的结果更新
        迭代式地添加元素
        []
        []->[A]
            ans: []  [A]
        []->[B],[A]->[A,B]
            ans:[]  [A]  [B]  [A,B]
        []->[C],[A]->[A,C],[B]->[B,C],[A,B]->[A,B,C]
            ans: []  [A]  [B]  [A,B]  [C]  [A,C]  [B,C]  [A,B,C]

        利用列表生成式可以简写为ans += [x + [item] for x in ans]
    复杂度分析：
        时间：NO2^N，第一层forON，第二层O2^(N-1)=O2^N,N-1是因为最后一次循环对2^(N-1)元素for循环添加
            最后一个元素行程O2^N个元素
        空间：O2^N，存储2^N个子集
    """
    ans = [[]]
    for num in nums:
        for exist in ans[:]:
            ans.append([num]+exist)
    #------------------------------------
    #for num in nums:
        #ans += [x + [num] for x in ans]
    return ans
if __name__ == '__main__':
    print(subsets2([1,2,3]))