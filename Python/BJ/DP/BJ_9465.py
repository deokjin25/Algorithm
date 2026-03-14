import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    cards = [list(map(int, input().split())) for _ in range(2)]

    # dp[0][i]: i열 위 선택, dp[1][i]: i열 아래 선택, dp[2][i]: i열 미선택
    dp = [[0] * n for _ in range(3)]
    dp[0][0] = cards[0][0]
    dp[1][0] = cards[1][0]
    dp[2][0] = 0

    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + cards[0][i]
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + cards[1][i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])

    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))