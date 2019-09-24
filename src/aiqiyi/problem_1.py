def solution(N,nums):


    ans = []
    remain = list(range(1,N+1))

    def dfs(index,path,remain,ans):
        if len(path) == N:
            #ans += 1
            ans.append(0)
            return
        for i in range(len(remain)):
            if len(path) > 0 :
                if (nums[index] == 1 and remain[i] < path[-1]) or ( nums[index] == 0 and remain[i] > path[-1]) :
                    dfs(index + 1,path + [remain[i]],remain[:i] + remain[i + 1:],ans)
            else:
                dfs(index + 1, path + [remain[i]], remain[:i] + remain[i + 1:], ans)
    dfs(-1,[],remain,ans)

    return len(ans)%(int(1e9)+7)
   # return len(ans)
"""

"""

# def solution(N,nums):
#
#     dp1 = [1] * N
#     dp2 = [0] * N
#     for i in range(1, N):
#         if nums[i - 1] == 0:
#             for j in range(i + 1):
#                 dp2[j] = sum(dp1[:j])
#         else:
#             for j in range(i + 1):
#                 dp2[j] = sum(dp1[j:i])
#         dp1, dp2 = dp2, dp1
#
#     return sum(dp1) % (int(1e9)+7)
def solution(N,nums):
    dp = [1 for _ in range(N)]
    for num in nums:
        if num == 1:
            dp = dp[1:]
            for i in range(len(dp)-1)[::-1]:
                dp[i] += dp[i + 1]
        else:
            dp = dp[:-1]
            for i in range(1, len(dp)):
                dp[i] += dp[i - 1]
    return dp[0] % (int(1e9)+7)
if __name__ == '__main__':

    N = int(input().strip())
    nums = list(map(int,input().strip().split(" ")))
    # N = 4
    # nums = [1,1,0]
    print(solution(N,nums))