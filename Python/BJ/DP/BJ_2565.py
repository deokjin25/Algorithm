import sys
input = sys.stdin.readline
from collections import defaultdict
from bisect import bisect_left

n = int(input())
a = defaultdict(int)
m = -1
for _ in range(n) :
  x, y = map(int, input().split())
  a[x] = y
  m = max(m, x)

dp = []
for i in range(1, m+1) :
  if a[i] != 0 :
    idx = bisect_left(dp, a[i])
    if idx == len(dp) :
      dp.append(a[i])
    else :
      dp[idx] = a[i]

print(n-len(dp))