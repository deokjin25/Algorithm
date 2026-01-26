# n, m = map(int, input().split())
# data = sorted(map(int, input().split()))

# def comb(depth, index, seq) :
#   if(depth == m) :
#     print(*seq)
#     return
  
#   for idx, val in enumerate(data) :
#     if(idx <= index) : continue
#     seq.append(val)
#     comb(depth+1, idx, seq)
#     seq.pop()

# comb(0, -1, [])

import itertools

n, m = map(int, input().split())
data = sorted(map(int, input().split()))

for c in itertools.combinations(data, m) :
  print(*c)