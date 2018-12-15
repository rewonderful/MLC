def ladderLength( beginWord, endWord, wordList):
    """
    Disscussion Method
    算法：生成&BFS
    思路：
                  3      4
                 dot -- dog
        1     2 / |      | \ 5
       hit -- hot |      | cog
                \ |      | /
                 lot -- log
        首先对问题的认识同XiaoXiangMethod，将问题构建为图，但是不同的地方是，这里直接生成所有可能的转换，
    即对一个word，依次将word[i]替换成别的字母形成新的单词new_one，再去判断new_one是否在not_visited中
        也就是说查找某个词可否转换的方式变成了用两层for循环，而不是生成图的数据结构在graph中遍历，然后用
        队列来保障进行的是BFS！
        设置队列word_q，num_q记录可以转化为的单词，以及到这步单词所用的step
        如果某次转换中某个词不能继续往下转了，那么就说明向下不可达，因为要到达目标单词的话要不停的循环，如果
        中间某一步就无法向下转化，word_q为空的话说明不能继续遍历，不可达
    复杂度分析：
        时间：O(len(word)*26)，时间复杂度主要取决于词的长度，XiaoXiangMethod在case29过不去
        空间：ON，两个queue和set的空间
    """
    import string
    hash_not_visited = set(wordList)

    if endWord not in hash_not_visited:
        return 0

    word_q = []
    num_q = []
    Find = False
    word = beginWord
    many = 0

    while not Find:
        for e in range(len(word)):
            for c in string.ascii_lowercase:
                new_one = word[:e] + c + word[e + 1:]
                if new_one in hash_not_visited:
                    word_q.append(new_one)
                    num_q.append(many + 1)
                    hash_not_visited.remove(new_one)
        if not word_q:
            many = 0
            break
        many = num_q.pop(0)
        word = word_q.pop(0)
        if word == endWord:
            Find = True
            many = many + 1

    return many

def ladderLength1(beginWord, endWord, wordList):
    """
    XiaoXiang Method
    ❌Python 超时了，
    思路：
        首先要将问题转化为合适的数据结构
            可以把转化的过程画出来，可以容易发现，这是一个图的结构
            因此用两个词能否转化来构建图
        构建好图后对图采用BFS找endWord，这个过程中用队列来维持状态，以及visit哈希表来记录是否访问过
        避免不必要的访问
        队列中记录的元素是word和到达当前word所用的step步数，即(word,step)
    """

    def check_link(s1, s2):
        if len(s1) != len(s2):
            return False
        else:
            diff_count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff_count += 1
            return diff_count == 1

    graph = [[] for _ in range(len(wordList))]
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if check_link(wordList[i], wordList[j]):
                graph[i].append(j)
                graph[j].append(i)
    queue = []
    visit = {beginWord: 1}
    for i in range(len(wordList)):
        if check_link(beginWord, wordList[i]):
            queue.append((i, 2))
            visit[wordList[i]] = 1

    while queue:
        i, step = queue.pop(0)
        if wordList[i] == endWord:
            return step
        for j in graph[i]:
            if wordList[j] not in visit:
                queue.append((j, step + 1))
                visit[wordList[j]] = 1
    return 0
if __name__ == '__main__':
    print(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))