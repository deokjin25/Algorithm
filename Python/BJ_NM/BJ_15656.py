# n, m = map(int, input().split())
# data = sorted(map(int, input().split()))

# def permR(depth, seq) :
#   if(depth == m) :
#     print(*seq)
#     return
  
#   for i in data :
#     seq.append(i)
#     permR(depth+1, seq)
#     seq.pop()

# permR(0, [])

import itertools

n, m = map(int, input().split())
data = sorted(map(int, input().split()))

for p in itertools.product(data, repeat=m) :
  print(*p)