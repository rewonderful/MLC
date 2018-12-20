"""

    重要的是了解什么是Trie树，前缀树，这个数的应用还是挺多的，将字符串组成的路径记录下来，以此来快速
    查找具有同一前缀的字符串！
    首先Trie树的每个节点本身不存储字符，是整个树的路径信息存储字符，每个节点有个标志位isWord来标识从根节点root到当前node
    节点的路径是否构成一个单词
    所以TrieNode每个节点有两个成员变量，
        其一是children,记录26个字符对应的子节点位置如
            {'a':nodeA,
             'b':nodeB,
             'c':nodeC,
             ...
             'y':None,
             'z':nodeZ}
        再者是isWord，记录当前节点node是否为一条路径上构成单词的位置
    理解了前缀树的数据结构后，就可以很方便地写出题目要求的4个函数了，因为Trie存储的是整棵树，所以要单独建TrieNode类，
    在Trie中存树的root节点，下面的操作也是对整棵树而言的
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        遍历word的每一个字符，检查Trie树中是否有，如果没有的话就新建节点，然后node前进到char代表的
        新的节点位置，最后走完之后node再word的最后一个char那里，置isWord = True
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    def search(self, word):
        """
        遍历word的每一个字符，如果某字符在遍历过程中Trie树中是没有的话，直接返回False，一直走啊走，走到最后
        说明Trie树中是有一条路径和word序列保持一致的，但是有这个路径不代表这个路径在Trie树中被标记为是一个词，
        所以return node.isWord
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isWord

    def startsWith(self, prefix):
        """
        和search有点相像，但是不一样的是，只要有这个prefix的路径，那么就一定有单词是以它为前缀的，所以OK，return True
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True