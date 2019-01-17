#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def rob(self, root):
    """
    My Method
    算法：DFS
    思路：
            首先这个，不可能用动规了，因为动规的话要用i来记录现在的状态和前序的状态，树形结构，没办法找到这种i和i-1
        的关系，所以就要考虑一般的做法了，一般的话，树的问题肯定是从遍历开始。遍历树类型的题，8成是递归，递归的话就先
        画一个最小的子树然后在考虑如何返回值和上面的节点关联起来。比如下面的这棵树
               4
              / \
             1   3
            对每个节点，只有抢或者不抢两种选择，先来看4，4如果抢的话，1和3就肯定不能抢了。如果4不抢的话，1和3，就是各自
        都可以抢或者不抢，即
            抢4的收益 = 4 + 1不抢的收益+3不抢的收益
            不抢4的收益 = max(1不抢3抢，1不抢3不抢，1抢3抢，1抢3不抢),也就是max(left_gain) + max(right_gain)
            所以对4来说，就能计算处 rot_root,not_rob_root两种收益
            并且可以将之return到上级，对整颗树而言，譬如下面的这个
                     3
                    / \
                   4   5
                  / \   \
                 1   3   1
            当已经知道3的左子树的情况，5的右子树的情况，那么再根据3抢或者不抢，就可以确定整个树的最大收益了，也就是说
        通过建立递归的关系，可以正确地在根节点处返回整棵树的最大收益，也正是因为这样，最后返回的是max(dfs(root))
    """

    def dfs(root):
        if root == None:
            return (0, 0)
        left_gain = dfs(root.left)
        right_gain = dfs(root.right)
        not_rob_root = max(left_gain) + max(right_gain)
        rob_root = root.val + left_gain[0] + right_gain[0]
        return (not_rob_root, rob_root)

    return max(dfs(root))
