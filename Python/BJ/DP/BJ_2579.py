n = int(input())
stair = [int(input()) for _ in range(n)]

if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0] + stair[1])
else:
    # dp[i][0] = i번째 계단을 1칸으로 올라온 경우 (i-1 밟음)
    # dp[i][1] = i번째 계단을 2칸으로 올라온 경우 (i-1 안 밟음)
    dp = [[0, 0] for _ in range(n)]
    
    dp[0][0] = stair[0]
    dp[0][1] = stair[0]
    dp[1][0] = stair[0] + stair[1]  # 0->1 (1칸)
    dp[1][1] = stair[1]              # 2칸 점프
    
    for i in range(2, n):
        # i-1을 밟고 온 경우: i-1은 반드시 2칸 점프로 왔어야 함
        dp[i][0] = dp[i-1][1] + stair[i]
        # i-2를 밟고 온 경우: i-2는 1칸/2칸 어느 쪽이든 가능
        dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + stair[i]
    
    print(max(dp[n-1][0], dp[n-1][1]))