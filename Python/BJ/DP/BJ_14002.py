import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
seq = list(map(int, input().split()))
dp = [ deque() for _ in range(n)]
#dp[x]: seq[x]를 끝으로 하는 가장 긴 수열
for i in range(n) :
  dp[i].append(seq[i])
  idx = -1
  l = 1
  for j in range(i,-1,-1) :
    if dp[i][0] > seq[j] :
      if l <= len(dp[j]) :
        idx = j
        l = len(dp[j])
  if idx != -1 :
    for k in range(len(dp[idx])-1, -1, -1) :
      dp[i].appendleft(dp[idx][k])
  
answer_idx = -1
answer_len = 0
for i in range(n) :
  if len(dp[i]) > answer_len :
    answer_len = len(dp[i])
    answer_idx = i
print(answer_len)
print(*dp[answer_idx])

# n = int(input())
# a = list(map(int, input().split()))
# length = [1]*n
# parent = [-1]*n

# for i in range(n):
#     for j in range(i):
#         if a[j] < a[i] and length[j]+1 > length[i]:
#             length[i] = length[j]+1
#             parent[i] = j

# best = max(range(n), key=lambda i: length[i])
# lis = []
# while best != -1:
#     lis.append(a[best])
#     best = parent[best]

# lis.reverse()
# print(len(lis))
# print(*lis)


# import sys, bisect
# input = sys.stdin.readline

# n = int(input().strip())
# a = list(map(int, input().split()))

# tails = []
# last_idx = []
# pos = [0]*n
# prev = [-1]*n

# for i, x in enumerate(a):
#     k = bisect.bisect_left(tails, x)
#     if k == len(tails):
#         tails.append(x)
#         last_idx.append(i)
#     else:
#         tails[k] = x
#         last_idx[k] = i

#     pos[i] = k + 1
#     if k > 0:
#         prev[i] = last_idx[k-1]

# # LIS 길이
# lis_len = len(tails)

# # LIS 마지막인덱스 찾기 (max pos)
# cur = max(range(n), key=lambda i: pos[i])

# res = []
# while cur != -1:
#     res.append(a[cur])
#     cur = prev[cur]
# res.reverse()

# print(lis_len)
# print(*res)