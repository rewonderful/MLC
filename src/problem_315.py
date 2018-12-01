#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def countSmaller( nums):
    """
    算法：分治/归并排序
    思路：
        利用分治的思想，归并排序时当前下标i后有多少个元素要把位置提到i之前就是其逆序数，
        在排序过程中记录逆序数的个数。⬅️其实比较难发现这个特征我觉着

        比如左右已经排序好的两个序列left = [-7,1,5,9],right = [-2,1,3,5]
            观察左右两个序列，以下描述中left中的值用i索引，right中的值用j索引
            对left和right中的元素，每个元素在当前位置的逆序数都是0，因为在本列表中，已经是
        从小到大排列的了，意味着右边不会有比自身小的数，但是二者进行归并排序的时候，两个数组
        之间会有大小的比较，进而产生逆序数
            在归并排序中，举例进行比较，
            当排序运行到过程i，j位置时
            如果left[i] <= right[j]:
                1. 在res中插入较小的元素left[i]，res.append(left[i])
                2. left[i]在left中的逆序数是0，因为left已排序，i后面的肯定比它大，所以此时
                看j在right中的情况，当left[i] <= right[j]时，因为归并排序是谁小谁就
                在前面，第j个位置的right比righ中的前j个元素大，即在前面的多次比较中，轮到
                第j个元素时，left[i] 才小于等于right[j]，说明之前left[i]都是大于right[0..j-1]的，
                否则在j之前left[i]就插入了，所以此时left[i]的逆序数就是right[j]的下标j
                3. 这里把等于的情况也放在这里是因为，对于两个元素相等时，逆序数的计算是和小于<时
                一样，所以把它放在<=这里，>的情况单独是else的另一类
                    其实以等于=的情况来看更清晰，在第i，j个位置处二者才相等，说明在right中该值
                    大于j个元素，那么left[i]的逆序数自然就是j了，而把相等的left[i]放进来后，后面right[j]
                    再进其逆序数也就自然而然是0了(res插入left[i]后，i++1，left和right中都至少大于
                    等于right[j]了)
            否则left[i] > right[j]:
                1. 在res中插入较小的元素right[i]，res.append(right[j])
                2. 由于right已经排序，right[j]必然小于j以后的元素，在right中逆序数是0，
                又因为right[j]比left[i]还要小，left中后面还会进行比较的元素一定大于left[i]，
                也就是说j这个位置的话，日后不论right还是left，都比当前j要大，逆序数是0

            当排序后left还有剩余的话，说明剩余的left元素每个元素都大于整个j的长度，
                如left=[5,6,7,8,9],right=[1,2,3,4,5],排序过程中一直插入right的值，最后left剩下的元素
                逆序数值+= right最后的j值，这个例子中最后j加到了5(所以才超出while的条件)

        注意：
                1. 排序的过程中会打乱下标，而最后返回的是原下标对应的逆序数计数值，所以在排序中行程原nums的pair
            对(nums[i],i)
                2. 逆序数的添加是+=，而不是单纯的 = ，上面的例子听起来似乎是用=，是因为这只是一次归并排序，实际上
            归并排序会迭代很多层，每一次迭代都是会让left和right变成一个新的排序后的组，而刚才也分析过了，对已经排序
            后的组，组内每个元素的逆序数是0，所以它们的逆序数值事实上是上一轮归并前计算的，所以每一层迭代下来逆序数
            的统计是+=

    复杂度分析：
        时间：ONlogN，归并排序的时间
        空间：ON，存储逆序数数组的大小
    """
    def mergesort(left, right, count):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                count[left[i][1]] += j
                i += 1
            else:
                result.append(right[j])
                j += 1
        for ii in range(i,len(left)):
            count[left[ii][1]] += j
            result.append(left[ii])
        if j < len(right):
            result.extend(right[j:])
        return result

    def merge(nums, count):
        if len(nums) < 2:
            return nums
        half = len(nums) // 2
        left = merge(nums[:half],count)
        right = merge(nums[half:],count)
        return mergesort(left, right, count)

    pairs = [(nums[i], i) for i in range(len(nums))]
    count = [0]*len(nums)
    merge(pairs, count)
    return count

if __name__ == '__main__':
    #print(countSmaller([9,8,7,6,5,4,3,2,1,0]))
    print(countSmaller([-1,-1]))