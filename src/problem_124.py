#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def maxPathSum(self, root):
    """
    Discussion Method
    算法：递归
    思路：
        要明确怎样可以取到path上的最大路径和
        某个节点node处，有这么三种状态，
            1.作为路径和的一部分
            2.作为路径和的结尾，其前导路径是左子树
            3.作为路径和的结尾，其前导路径是右子树
            如果将之转化为路径和的角度来看的话，如果左子树最大和<0，右子树最大和<0，就会有第四种情况
            4.作为路径和的结尾，其左右子树都不选取，因为左右子树的和<0
        那么经过某一节点的最大路径和就一定在这四种情况中 max( case_1,case_2,case_3,case_4 )

        ans = max(ans,left+right+root.val,left+root.val,right+root.val,root.val)

            联想以前做的maxPathSum，如果前导路径，or 左右子树的最大和，是负数，那就直接当没有左右子树好了
            也就是说left_max = max(0,getMax(root.left))
            所以上面的max比较中， 可以不去比较4个这么多，直接max(ans,left+right+root.val)就好了，这样就已经
        囊过上面的4种所有情况的比较了，此时便可以得到，如果以某个节点为最大路径和的一部分时的最大值

        ❗️❗️❗️：
            要注意函数的返回值，函数返回的是代表当前节点作为头部节点的情况下，子树路径的最大和，譬如下面这个树
                   -10
                   / \
                  9  20
                    /  \
                   15   7
            20这个节点，在计算其为最大路径一部分的时候，当然会考虑20在路径中了，
            也就是：左15 根20 右7
                但是由于路径上是不能有回溯的，每个节点一定是遍历一次，即不可能有-10 20 15 20 7 这样的路径，如果
            -10 要把20 15 7都囊括进来的话，是不对的。无法将路径拉成一条平的path，一条平的path遍历时一定是没有回溯
            关系的。比如9,-10,20,7或者9,-10,20,15这样才是合法的路径
                所以当前函数执行完时，应该返回max(left,right) + root.val，即以当前节点作为一段序列和的末尾，这个
            节点的左子树或者右子树作为其前导or(后导)路径，并且只能选择一条，所以是max(left,right) + root.val
    """
    self.curr_max = float('-inf')
    def getMax(root):
        if root == None:
            return 0
        left = max(0,getMax(root.left))
        right = max(0,getMax(root.right))
        self.curr_max = max(self.curr_max , left + right + root.val)
        return max(left,right)+root.val
    getMax(root)
    return self.curr_max