import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * (n + 2)

max_fixed = 0

for v in arr:
    dp[v] = dp[v - 1] + 1
    max_fixed = max(max_fixed, dp[v])

print(n - max_fixed)