#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def pathSum(self, root, sum):
    """
    Disscusion Method
    算法：哈希表+DFS
    思路：
        首先要想暴力解法是怎样进行的
            在暴力解法中，也就是下面我的那种解法，遍历每一个节点，在每一个节点的位置，还要向下遍历其他的每一个节点
        但是这样的话在遍历的过程中有很多遍历是重复的
                              10
                             /  \
                            5   -3
                           / \    \
                          3   2   11
                         / \   \
                        3  -2   1
            比如遍历到5的时候。会有5->3->3，3->3，10->5->3->3，其实就是一条路径，只不过每次的节点不一样罢了。
        但是用暴力解法遍历的话会重复遍历很多次，例如以10开头的时候遍历了10->5->3->3，后面又会以5开头遍历5->3->3
            所以首先要想的是，如何将一条路径拆成多条，因为根据题意，答案的路径不一定非要是从root开始的，所以在遍历
        过程中形成的path路径，能不能将他拆开？比如从10开始遍历，遍历路径10->5->3,能不能将其拆成10,5->3？
            答案当然是可以的，因为可以看做是从10出发了3层到达的这里，其实第一层10的时候就可以记录下来这个10，然后到
        10->5->3的时候，再"减去"前面单个节点10的情况就好了。
            所以这种解法就是基于这样的思想在遍历所有节点。并且联想TwoSum中的做法，用哈希表来存储要找的那个"加数"
            注意到本题中，要求的解的路径其实可以看做是一整条路径中的一部分，然后再根据上面讲到的将一条路径拆成多个
        部分组成。那么就可以设置一个哈希表，record，由record记录当前路径和的个数，{curr_sum:counter},
            由curr_sum来记录遍历到当前节点的路径和，如果一条目标路径在这条路径中，那么就可以按上述的拆分路径的方法求得
        当前子路径的前序路径和，即prefix_sum = curr_sum - target,然后在record中查询prefix_sum的个数。如果record
        中记录了这个prefix_sum，那么就表明当前路径中包含解，并且prefix_sum有几个，这样的路径就有几个
            如：10->5->3,target = 8，curr_sum - 8 = 10，而前面记录下来的record[10]=1，就说明有1条包含答案的路径，
        当然了，如果前面record[10]=n，那么就说明走到了10->5->3时，在这条路径上符合答案的路径就有n条，result += n
            所以在遍历的过程中应该record[curr_sum] += 1,记录下来curr_sum的个数，curr_sum在后面层数的递归中就相当于
        是prefix_sum了。
            所以根据以上思路dfs前序遍历二叉树，并且要注意的是当前节点的左右子树遍历完之后，要record[curr_sum] -= 1
            因为记录record[curr_sum] -= 1是为了记录当前路径和作为prefix的话有多少个，当前节点的子树遍历完之后，应该
        弹出当前节点的路径和，就像回溯的时候一样。比如还是10->5->3这里，记录了18后，遍历完这个③的节点，将18的个数减1，
        避免递归到⑩的右子树时，可能某个位置需要前面是18，但是误认为左子树的③这里记录的18是符合要求的，这样会将路径
        计算错。
            ❗️❗️❗️所以要明确，record[curr_sum]记录的是当前路径上有多少个子前缀路径的和是curr_sum，或者从子递归中看，应该叫
        record[prefix_sum]
    复杂度分析：
        时间：ON，遍历一遍所有节点
        空间：ON，哈希表空间
    """
    self.result = 0

    def dfs(root, record, curr_sum):
        if root == None:
            return
        curr_sum += root.val
        prefix_sum = curr_sum - sum
        if prefix_sum in record:
            self.result += record[prefix_sum]
        record.setdefault(curr_sum, 0)
        record[curr_sum] += 1
        dfs(root.left, record, curr_sum)
        dfs(root.right, record, curr_sum)
        record[curr_sum] -= 1

    dfs(root, {0: 1}, 0)
    return self.result



def pathSum1(self, root, sum):
    """
    My Brute Force Method
    算法：暴力
    思路：
        Do as they say
        遍历所有可能，dfs遍历每个节点，在每个节点位置向下深度遍历calculateSum()计算是否构成题解
        这里主要是会重复计算一些路径和，导致时间的浪费
    复杂度分析：
        时间：ON2
        空间：ON2
    """
    self.counter = 0
    def calculateSum(root,path_sum):
        if root == None :
            return
        path_sum += root.val
        if path_sum == sum:
            self.counter += 1
        calculateSum(root.left,path_sum)
        calculateSum(root.right,path_sum)
    def dfs(root):
        if root == None:
            return
        calculateSum(root,0)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return self.counter