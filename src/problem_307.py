#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class NumArray:
    """
    算法：分段树 SegmentTree
    思路：
        将nums每次对半分段，构建分段树，分段树节点存储nums[left,right]的区间和
        分段树：
            线段树是一种平衡二叉搜索树(完全二叉树)，它将一个线段区间划分成一些单元区 间。对于线段树中的每一个非叶子节
        点[a,b]，它的左儿子表示的区间为[a,(a+b)/2]，右 儿子表示的区间为[(a+b)/2+1,b]，最后的叶子节点数目为N，与
        数组下标对应。线段树 的一般包括建立、查询、插入、更新等操作，建立规模为N的时间复杂度是 O(NlogN)，其他操作时
        间复杂度为O(logN)。
            分段树是完全二叉树，可以用一维数组存储
    """
    def __init__(self, nums):
        """
        建立分段树：
            由于分段树最顶层的根节点存储的是[0,len(nums)]的区间和左子树存储的是[0,len(nums)/2]的区间和，
        右子树存储[len(nums)/2+1,len(nums)]区间和，以此类推，所以可以用递归的方式建立

                                [0,len(nums)-1]
                                 /           \
                        [0,len(nums)/2]     [len(nums)/2+1,len(nums)]
                               /              \
                            ....              ....
            如果用TreeNode的结构，TreeNode应该是如下形式：
                class SegmentTreeNode:
                    self.segment_sum = X
                    self.left_segment = i
                    self.right_segment = j
                    self.left_child = None
                    self.right_child = None
            由于这里用一维数组来实现，而上述SegmentTreeNode的内容又都必须包括，就需要在递归的过程中，计算并传递left，right
        而segemnt_sum则可以用values一维数组来存储，其中valuse的下标pos来表征当前节点与左孩子和右孩子的关系，
            当前节点的下标为pos，则:
                left_child at --> pos*2+1
                right_child at --> pos*2+2
            所以在建立过程中，如果left == right，则说明抵达了叶子节点，values[pos] = nums[left]
            否则的话，找到[left,right]的中间位置mid进行左右子树分割，左子树的区间段是[left,mid]，右子树的区间段是[mid+1,right]
            计算出左子树和右子树的segment_sum后，当前pos位置的segment_sum值= values[left_pos]+values[right_pos]
        """
        if nums == []:
            return
        self.nums_end = len(nums) - 1
        self.values = [0] * 4 * len(nums) #小象学院PDF说一般线段树数组长度是原len(nums)的4倍

        def build_segment_tree(pos, left, right):
            if left == right:
                self.values[pos] = nums[left]
                return
            mid = (left + right) // 2
            build_segment_tree(pos * 2 + 1, left, mid)  # left child at pos*2+1
            build_segment_tree(pos * 2 + 2, mid + 1, right)  # right child at pos*2+2
            self.values[pos] = self.values[pos * 2 + 1] + self.values[pos * 2 + 2]

        build_segment_tree(0, 0, self.nums_end)

    def update(self, i, val):
        """
        更新分段树
            分段树虽然存储的是区间分段的和，但是分段树的叶子节点就是存储的nums中每个元素的值，对应于left==right的时候
            所以更新某个元素值时，递归地从下到上进行更新
             if left == right and left == i:
                更新pos的values = val
            否则求重点mid尽心分割，更新左右子树，
            values[pos] = 左子树和+右子树和
        """

        def update_segment_tree(pos, left, right):
            if left == right and left == i:
                self.values[pos] = val
                return
            mid = (left + right) // 2
            if i <= mid:
                update_segment_tree(pos * 2 + 1, left, mid)
            else:
                update_segment_tree(pos * 2 + 2, mid + 1, right)
            self.values[pos] = self.values[pos * 2 + 1] + self.values[pos * 2 + 2]
        update_segment_tree(0, 0, self.nums_end)

    def sumRange(self, i, j):
        """
        求[i,j]区间和
            当建立分段树后，求[i,j]区间和就比较顺畅了，将[i,j]从根节点向下遍历并分段，不断求得子区间的值并且sum起来即是答案
        在向下递归求和的过程中要注意递归的出口，其实也就是左右区间分段的原则,要注意在每次向下递归的时候，比较的是i,j与当前
        节点的left,right的关系来决定子分段和的值
            if [i,j] [left,right ] or [left,right] [i,j] i,j在left，right以外的位置
                return 0
            if [i,[lef,right],j] 如果left,right 在i，j内，
                return values[pos]  left，right内有多少返回多少
            否则的话说明 i,left,..,j,..right,ij与left,right是有部分有交集的，则对当前left,right区间通过中点mid进行分割
                return 左侧和+右侧和
        """

        def sum_range_segment_tree(pos, left, right):
            if i > right or j < left:
                return 0
            if left >= i and right <= j:  # 线段树当前范围[left,right]在所求区间[i,j]中则返回当前这个pos处的values
                return self.values[pos]
            mid = (left + right) // 2   #否则说明线段树当前pos的[left,right]的范围是d大于[i,j]的，需要分割
            return sum_range_segment_tree(pos * 2 + 1, left, mid) + sum_range_segment_tree(pos * 2 + 2, mid + 1, right)

        return sum_range_segment_tree(0, 0, self.nums_end)

if __name__ == '__main__':
    test = NumArray([0,1,2,3,4,5])
    print(test.sumRange(3,4))
