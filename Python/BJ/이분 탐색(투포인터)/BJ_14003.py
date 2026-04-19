import sys
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))

lis = []
pos = []

for x in seq :
  idx = bisect_left(lis, x)
  if idx == len(lis) :
    lis.append(x)
  else :
    lis[idx] = x
  pos.append(idx)

length = len(lis)
target = length - 1
result = []

for i in range(n-1, -1, -1) :
  if pos[i] == target :
    target -= 1
    result.append(seq[i])

result.reverse()
print(length)
print(*result)
