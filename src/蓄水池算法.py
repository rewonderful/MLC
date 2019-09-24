#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
    算法思路大致如下：

    1. 如果接收的数据量小于m，则依次放入蓄水池。
    2. 当接收到第i个数据时，i >= m，在[0, i]范围内取以随机数d，若d的落在[0, m-1]范围内，则用接收到的第i个数据替换蓄水池中的第d个数据。
    3. 重复步骤2。
    算法的精妙之处在于：当处理完所有的数据时，蓄水池中的每个数据都是以m/N的概率获得的。

    下面用白话文推导验证该算法。假设数据开始编号为1.

    第i个接收到的数据最后能够留在蓄水池中的概率=第i个数据进入过蓄水池的概率*之后第i个数据不被替换的概率（第i+1到第N次处理数据都不会被替换）。

    1. 当i<=m时，数据直接放进蓄水池，所以第i个数据进入过蓄水池的概率=1。
    2. 当i>m时，在[1,i]内选取随机数d，如果d<=m，则使用第i个数据替换蓄水池中第d个数据，因此第i个数据进入过蓄水池的概率=m/i。
    3. 当i<=m时，程序从接收到第m+1个数据时开始执行替换操作，第m+1次处理会替换池中数据的为m/(m+1)，会替换掉第i个数据的概率为1/m，
        则第m+1次处理替换掉第i个数据的概率为(m/(m+1))*(1/m)=1/(m+1)，不被替换的概率为1-1/(m+1)=m/(m+1)。依次，第m+2次处
        理不替换掉第i个数据概率为(m+1)/(m+2)...第N次处理不替换掉第i个数据的概率为(N-1)/N。所以，
        之后第i个数据不被替换的概率=m/(m+1)*(m+1)/(m+2)*...*(N-1)/N=m/N。

    4. 当i>m时，程序从接收到第i+1个数据时开始有可能替换第i个数据。则参考上述第3点，之后第i个数据不被替换的概率=i/N。
    5. 结合第1点和第3点可知，当i<=m时，第i个接收到的数据最后留在蓄水池中的概率=1*m/N=m/N。结合第2点和第4点可知，
        当i>m时，第i个接收到的数据留在蓄水池中的概率=m/i*i/N=m/N。综上可知，每个数据最后被选中留在蓄水池中的概率为m/N。
"""
import random
def tank_sample(k,data_stream):
    sample = [0] * k
    for i in range(len(data_stream)):
        if i < k:
            sample[i] = data_stream[i]
        else:
            rand = random.randint(0,i)
            if rand < k:
                sample[rand] = data_stream[i]
    return sample


if __name__ == '__main__':
    k = 10
    N = 100
    data_stream = list(range(N))
    statistic = [0]*N
    for _ in range(10000):
        sample = tank_sample(k,data_stream)
        for i in sample:
            statistic[i] += 1
    import matplotlib.pyplot as plt
    plt.plot(statistic)
    plt.show()
    #print(statistic)