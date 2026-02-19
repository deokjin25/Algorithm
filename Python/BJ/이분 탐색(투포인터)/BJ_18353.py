import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
soldiers = list(map(int, input().split()))
dp = []
for soldier in soldiers :
  idx = bisect_left(dp, -soldier)
  if idx == len(dp) :
    dp.append(-soldier)
  else :
    dp[idx] = -soldier

print(n - len(dp))