import sys
input = sys.stdin.readline
from bisect import bisect_left

n=int(input())
seq = list(map(int, input().split()))
lis = []

for x in seq :
  idx = bisect_left(lis, x)
  if idx == len(lis) :
    lis.append(x)
  else :
    lis[idx] = x

print(len(lis))