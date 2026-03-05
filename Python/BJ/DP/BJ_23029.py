# n = int(input())
# dp = [[0,0] for _ in range(n) ]
# dp[0][0] = int(input())

# if n > 1 :
#   food = int(input())
#   dp[1][0] = food
#   dp[1][1] = dp[0][0] + food//2

# for i in range(2, n) :
#   food = int(input())
#   dp[i][0] = max(dp[i-2][0] + food, dp[i-2][1] + food)
#   dp[i][1] = max(dp[i-1][0] + food//2, dp[i-1][1] + food//2)

# print(max(dp[-1][0], dp[-1][1]))

n = int(input())
dp = [[0,0,0] for _ in range(n) ] #[0]: 안 먹음, [1]: 먹음. [2]: 절반 만 먹음
dp[0][1] = int(input())

for i in range(1, n) :
  food = int(input())
  dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
  dp[i][1] = dp[i-1][0] + food
  dp[i][2] = dp[i-1][1] + food//2

print(max(dp[-1][0], dp[-1][1], dp[-1][2]))
