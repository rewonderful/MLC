#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def combinationSum( candidates, target):
    """
    算法：递归/回溯
    思路：
            像求子集一样，需要遍历所有的可能情况，而while，for这样的循环都是某种意义上的"定循环"，循环
        的"次数"是固定的，这里打引号是因为，while的次数可以不定，但是for和while都是一层循环，应该用这
        个词描述比较好，都是单层循环，而递归可以嵌套，根据递归的条件可以构造不定次循环。,◀️这是关键
            OK，看这道题
            其实就是要把所有可能的状态都去试一下，很容易联想到用递归，每次算的时候都去找小于target的
        candidates中的元素，添加到【临时列表】中，只有最后这些临时列表中的元素和等于target才应该把
        它们添加到result中，所以递归的时候应该向下一层循环传入的target应该为target-curr_num，以及
        当前的路径path情况。
            这里要注意为了避免重复，请联想twoSum，treeSum那些题的思路，出现重复的原因是前面用过了后面还要用，
        譬如[4,2,8]->8，如果每次向后传入的都是最原始的candidate整个列表，会出问题，如：
            当前判定的num是4,根据算法，会得到一组[4,2,2]的解
            当前判定的num位2时，如果这时遍历的列表还是[4,2,8]，那么就会产生[2,2,4]的解，与前面重复了
            所以，关键就是，如果前面的元素i和后面的元素j通过组合能形成解(毕竟这个解不管ij的排列顺序)，那么
        在以i判定的时候，就一定会解出所有ij可以构成的解（况且本题还允许各个位置的数字自身重复）。那么去重
        的方式就是在后面判定的时候，传入的是当前位置开始的数组的切片，candidates[i:]，这样在判定当前位置i
        的后续组成元素时，就不会去找i之前的元素了，避免了重复，达到了【剪枝】的效果
    ps:看别人的题解基本都用了排序来去重，其实我这种解法，通过传入当前位置后的切片这个思想就可以避免排序的操作达到去重的效果
    复杂度分析：
        时间：不会算。。反正肯定大于ON2小于ON2^N
        空间：不会算。。反正肯定大于ON2小于ON2^N
    """

    def find(candidates, target, path, result):
        if target < 0:
            return
        for i in range(len(candidates)):
            curr_path = path + [candidates[i]]
            if candidates[i] == target:
                result.append(curr_path[:])
            if candidates[i] < target:
                find(candidates[i:], target - candidates[i], curr_path[:], result)

    result = []
    find(candidates, target, [], result)
    return result
if __name__ == '__main__':
    print(combinationSum([4,2,8],8))