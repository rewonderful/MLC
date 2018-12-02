#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.ancestor = None

    def lowestCommonAncestor(self, root, p, q):
        """
        My Method
        算法：深搜
        思路：
                首先要明确，最近的公共祖先一定是第一次回溯时可以判定是他俩祖宗的那个。比如5是6和2的最近祖先
            那么在遍历完左右子树后在看5这个节点的状态就可以判断是不是祖先了，并且第一次是祖先的就是最近的那个，
            比如这里5是62的祖先，3也是，但是回溯的时候先到5，所以5是目标解
                _______3______
               /              \
            ___5__          ___1__
           /      \        /      \
           6      _2       0       8
                 /  \
                 7   4
            而且祖先一定是以下两种方式之一：
                左子树含pq一个，右子树含pq一个
                自己是就是pq中的一个，左右子树中含pq中的一个
            故在遍历的时候，对当前节点root，设置curr判断root是不是含pq中的一个，然后
                对左子树遍历，看左子树中是否含pq中的一个
                对右子树遍历，看右子树中是否含pq中的一个
            回溯到本节点root时，得到三组[bool,bool]对，对三组bool对0，1位置分别or运算看看
            当前root处是否record都为True，是的话说明该节点处包含了pq，并且如果此时全局变量ancestor==None
            的话说明是第一个遍历到的祖先，即可以设置
                要注意的是这里分了三个部分，curr,left,right而不把curr的状态传给子树是因为，如果当前节点
            是pq中的一个，得到[T,F]，将[T,F]向子树传递的过程中若子树V的位置中找到了[F,T],那么由于V处达到了[T,T],
            会判定V为祖先,然而事实上应该是root处。故不向下传递curr状态
                叶子节点return[F,F]是因为False的or运算不影响父节点[bool,bool]的状态

        复杂度分析：
            时间：ON，遍历所有节点
            空间：ON，遍历节点的递归栈空间
        """
        def dfs(root):
            if root == None:
                return [False, False]
            curr = [root == p, root == q]
            left = dfs(root.left)
            right = dfs(root.right)

            record = [(left[0] or right[0] or curr[0]), (left[1] or right[1] or curr[1])]
            if record[0] and record[1] and self.ancestor == None:
                self.ancestor = root
            return record
        dfs(root)
        return self.ancestor

    def lowestCommonAncestor2(self, root, p, q):
        """
        算法：深搜
        思路：
            与My Method相近，但是不会直接记录每个节点处的[bool,bool]状态，
            注意最近祖先的特征：
                祖先一定是以下两种方式之一：
                    1.左子树含pq一个，右子树含pq一个
                    2.自己是就是pq中的一个，左右子树中含pq中的一个
            对每个位置判断当前节点是不是p,q，是的话直接返回该节点，否则判断其左右子树
            如果左子树和右子树都不为空的话，符合子树条件1，return root
            否则的话，左右子树哪个返回的不为None返回哪个，为None就不说了，肯定不是解
            除非左右都为None，那肯定就返回None，代表该root不是其祖先
            但是如果有一个不是None的话说明那个非None的节点就是其祖先节点，并且由于
            return会立马结束函数的执行，可以说return保障了返回的是最近祖先
                如下图，找7，4的祖先，3右侧是None，左侧返回5的返回结果，5的左侧是None
            右侧非None，返回右子树的结果，而右子树返回的恰恰就是2，因为在2处，其左右都非None
            使得在2的位置return 2，递归return 回去最后return回的就是2
                        _______3______
                       /              \
                    ___5__          ___1__
                   /      \        /      \
                   6      _2       0       8
                         /  \
                         7   4
        复杂度分析：
            时间：ON，遍历所有节点
            空间：ON，遍历节点的递归栈空间

        """
        if not root:
            return None
        if root == p or root == q:
            return root
        left_ances = self.lowestCommonAncestor(root.left, p, q)
        right_ances = self.lowestCommonAncestor(root.right, p, q)
        if left_ances and right_ances:
            return root
        else:
            if left_ances != None:
                return left_ances
            if right_ances != None:
                return right_ances
            return None

    def lowestCommonAncestorFail(self, root, p, q):
        """
        小象学院pdf上的题解，但是TLE了，不过思路挺直观的！
        找到p从根节点开始的路径p_path
        找到q从根节点开始的访问路径q_path
        求出p_path,q_path中较小的长度
        遍历p_path与q_path，ancestor等于最后一个相等的节点，即最后，最近的公共祖先
        """
        def getpath(root, path, pathes):
            if root == None or len(pathes) == 2:
                return
            if root == p or root == q:
                pathes.append(path + [root])
            getpath(root.left, path + [root], pathes)
            getpath(root.right, path + [root], pathes)

        pathes = []
        getpath(root, [], pathes)
        p_path, q_path = pathes
        ancestor = None
        min_len = min(len(p_path), len(q_path))
        for i in range(min_len):
            if p_path[i] == q_path[i]:
                ancestor = p_path[i]
            else:
                break
        return ancestor
if __name__ == '__main__':
    # [5,4,8,11,null,13,4,7,2,null,null,null,1]

    # n1 = TreeNode(5)
    # n2 = TreeNode(4)
    # n3 = TreeNode(8)
    # n4 = TreeNode(11)
    # n5 = TreeNode(13)
    # n6 = TreeNode(4)
    # n7 = TreeNode(7)
    # n8 = TreeNode(2)
    # n9 = TreeNode(1)
    #
    # n1.left = n2
    # n1.right = n3
    # n2.left = n4
    # n4.left = n7
    # n4.right = n8
    # n3.left = n5
    # n3.right = n6
    # n6.left = n9
    #[3,5,1,6,2,0,8,null,null,7,4]
    n1 = TreeNode(3)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    n4 = TreeNode(6)
    n5 = TreeNode(2)
    n6 = TreeNode(0)
    n7 = TreeNode(8)
    n8 = TreeNode(7)
    n9 = TreeNode(4)

    n1.left = n2
    n1.right = n3
    n2.left=n4
    n2.right=n5
    n5.left=n8
    n5.right=n9
    n3.left=n6
    n3.right=n7
    s = Solution()
    print(s.lowestCommonAncestor0(n1, n2,n3))