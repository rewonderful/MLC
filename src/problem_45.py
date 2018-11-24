#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def jump_0(self, nums):
    """
    算法：贪心
    思路：
        首先要注意到：
            题设是一定可以从头部节点到达尾部节点，和55题类似，如果一个节点可以从i到达j，那么一定可以到达i和j中间
        的任何一个节点i,i+1.i+2,...,j-1,j。同理，这里的题设已经使得数组从0开始一定可以一步一步从0,1,2,3...last
        抵达last节点，也就是从0开始一步一步就遍历数组一定是正确的遍历方式，关键在于何时跳跃，跳跃几次
        何时跳跃？
            在逐个遍历数组的过程中，到达某一位置时，发现从当前位置起跳无法到达更远的位置，由于从0开始一定能到达最
        后一个位置，那么就意味着在当前位置之前，必然有1次跳跃，且跳跃到更远的位置，事实上在该位置之前有多个可以跳
        越到更远位置的地方，那么应该选择跳到哪里？(这时候起跳位置就不重要了，重要的是能跳到哪里去，因为这里要记录的
        是跳跃的次数，并不是跳跃的位置，当然了如果要求跳跃的序列，也可以记录下来，问题不大)。答：应该跳值最远的那个
        地方，贪心的思想

        SO:
            1. 设置jump_before_end 记录最小跳跃次数，注意这里初始值为1，它代表的是到达last前必要的跳跃次数
                经过某个位置后才发现该位置不能跳更远的位置才记录的过去应该有一次跳跃，像一根绳子分3段要切2刀
            2. 设置pre_max_reach记录已遍历位置中最远可达位置
               curr_max_reach 为从头开始遍历的过程中整个过程里最远可达位置的变化情况，i就是和这个比较
            3. i 遍历所有位置，用pre_max_reach更新已经遍历过的这一段中最远可达位置，curr_max_reach跟踪
               整个遍历过程中的最远可达位置，当前位置i>当前整个过程的curr_max_reach时则应该jump+1表明
               在此之前必然有一次跳跃，并且更新curr_max_reach
    复杂度分析：
        时间：ON，遍历一次数组
        空间：O1，常数级
    """
    if len(nums) < 2:
        return 0
    jump_befor_end = 1
    pre_max_reach = nums[0]
    curr_max_reach = nums[0]
    for i in range(1, len(nums)):
        if i > curr_max_reach:
            jump_befor_end += 1
            curr_max_reach = pre_max_reach
        pre_max_reach = max(pre_max_reach, i + nums[i])
    return jump_befor_end


def jump_1(nums):
    """
    算法：与jump_1 思路类似，贪心
    思路：
            将遍历过程（跳跃过程，因为0到last可达，故可达0,1,2..last任何一个位置，所以可以遍历）看做是一段一段的
        每一段都跳到最远可达的那个位置

            记录当前遍历的情况，记录当前可达最远距离curr_farthest,在遍历数组的过程中更新curr_farthest，
        如果已经抵达当前段的最远位置，再往后走就要跳了，所以counter += 1，更新下一段最远可达位置为之前记录的
        最远可达位置，类似jump_0中的curr_max_reach = pre_max_reach

            这里的range只到len(nums)-1是因为，程序只要在到达end时就会+1，由于必然会跳到最后一个节点，那么如果
        条件是 range(len(nums))，则会抵达了最后一个节点，出发i == curr_end 的判断条件，由此一来程序会认为
        最后一个节点处又要开始起跳，counter += 1,会多加一次不必要的跳跃，所以遍历到last-1位置即可

        与jump_0对比：
            二者其实非常相似，都是记录当前的遍历情况和跳跃情况
            但是jump_0关注的是【超过】跳跃点之后，即继续往下无法到达更远的位置，那么在之前会有一次跳跃，因此counter += 1
            jump_1关注的是当前的遍历和跳跃情况，如果我遍历到了【本段】的最后一个位置，那么就应该跳跃到下一个更远的位置去

            所以要注意二者counter += 1 的时刻，条件，背景是与意义是不相同的

    复杂度分析：
        时间：ON，遍历一次数组
        空间：O1，常数级
    """
    counter = 0
    curr_end = 0
    curr_farthest = 0
    for i in range(len(nums)-1):
        curr_farthest = max(curr_farthest, i + nums[i])
        if i == curr_end:
            counter += 1
            curr_end = curr_farthest
    return counter
"""
从Details中看的一个submit，不是很直观，也没细看
 if not nums or len(nums) <= 1:
            return 0
        slow, fast = 0, 0
        step = 0
        last = len(nums) - 1
        while slow <= fast:
            step += 1
            old_fast = fast
            for i in range(slow, fast+1):
                fast = max(fast, i + nums[i])
                if fast >= last:
                    return step
            slow = old_fast + 1
        return 0
"""
if __name__ == '__main__':
    print(jump_1([2,3,1,1,4]))