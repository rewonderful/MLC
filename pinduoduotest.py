def solution(n, heights):
    if n <= 2:
        return 0
    dp_climp = [0] * n
    dp_jump = [0] * (n + 1)

    dp_climp[0], dp_climp[1] = heights[0], heights[1]
    dp_jump[0], dp_jump[1] = 0, 0

    for i in range(2, n + 1):
        if i < n:
            dp_climp[i] = min(dp_jump[i - 1], dp_climp[i - 1]) + heights[i]
        dp_jump[i] = min(dp_climp[i - 1], dp_climp[i - 2])

    return min(dp_climp[-2], dp_jump[-1], dp_jump[-2])


if __name__ == '__main__':
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input().strip()))
    print(solution(n, nums))