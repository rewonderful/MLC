#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    算法：利用Trie树
    思路：
        存这种字符串类型的数据，Trie树是一个比较适当的数据结构，所以联想208题建立Trie树的过程，可以比较
        轻松地选定数据结构，并且写好addWord
        难点和关键在于search这里，主要是search中的'.'该如何处理

            其实比较容易想到的思路就是用dfs，结合208题正常Trie树的search，在正常的Trie树中搜索字符串的
        时候，对某个字符char，向下只会走一条道路，或者无路可走，可以比较直观地找到路径，这里有通配符'.'后，
        就是要向下走所有可能的子节点，b.d，在某个node处，node的children={'a':x1,'c':x2，'e':x3},则
        b.d可以向下可以有x1,x2,x3三个子节点可以走，而一个特定的单词如bad，就只能走x1，相当于一个不含
        '.'的位置，向下走的选择只有1个或者0个，而含'.'的位置，向下可以走所有
            [next_node  for next_node in node.chilren.values()]
            所以自然地选择用dfs来做，这里dfs的难点在于终止位置、条件，以及如何恰当地构造出递归的关系
            首先是程序参数， 一种比较自然的想法就是每次在乎当前要判断的字符以及当前所在节点，所以考虑root,i
        先不管程序出口(二叉树中root == None ,return None 这种)
            先区分word[i] 是否为'.' ,是的话，递归遍历所有可能子节点，否则的话，只有当word[i] in node.children，
        才递归。
            如何向下递归？
                首先要明确这里建立dfs的作用：dfs来判断当前root，和当前word[i]下是能否查得到词，所以返回是bool类型的
                (并且可以递归地来看查词这个事儿'bad'这个词查询，可以分解为'b'->'a'->'d')
                所以条件应该是if dfs(next_leve) == True， return True，否则，就等所有情况都不满足，都没有return True
                的话，再return False，这里的逻辑是，如果都没有，才False
            如此便可以根据此在word[i] 是否为'.'构建递归
            但是还不够，还需要确定程序递归到底层的出口，由于i每次向下+1，也就是每层递归是考虑下一个位置的i则最后如果i==len(word)，
        就说明判断到最后一个位置的字符之后了，为什么说之后&是i==len(word)？因为Trie树当前节点children保存的是下一层的节点地址，
        如bad,判断到d了，是'd' in curr_node.children，所以还要dfs到next_node中，即'd'指向的next_node位置，判断next_node.isWord，
        符不符合查询，直接return next_node.isWord即可
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool

        """

        def dfs(node, i):
            if i == len(word):
                return node.isWord
            if word[i] == '.':
                for next_node in node.children.values():
                    if dfs(next_node, i + 1):
                        return True
            else:
                if word[i] in node.children:
                    if dfs(node.children[word[i]], i + 1):
                        return True
            return False

        node = self.root
        return dfs(node, 0)


