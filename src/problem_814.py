#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def pruneTree(self, root):
    """
    算法：递归遍历
    思路：
        本题思路比较直观，用递归去做，遍历的时候进行剪枝
            怎样算剪枝？➡️把root的left or right 置None即可
        故核心就是看什么时候剪枝，在剪枝的时候把root左右置None即可
        剪枝，或者说将其视为None的条件也很明确，一个节点左右都是None并且它自己的val是0，就
        应该剪掉这个节点，或者说递归的当前层返回None，否则就是正常返回root
            一开始我在考虑剪枝的时候吧if root.val==0那一长串放到了if root == None底下，
        后来发现只是这样的话,这种情况就会剩下根节点的0，按理说应该整个都剪掉的，所以底下还要
        在用if root.val==0那一长串再进行一次判断剪枝，那这样还不如只放一次，放在后面，并且
        可以自己根据逻辑推一遍，的确是只放一次放到后面就行了，这样会逐层剪枝
                     0
                   /  \
                  0    0
    复杂度分析：
        时间：ON，遍历所有节点
        空间：ON，递归栈空间
    """
    if root == None:
        return None
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)
    if root.val == 0 and root.left == None and root.right == None:
        return None
    return root