# n,m = map(int, input().split())
# data = sorted(map(int, input().split()))

# def permR(seq) :
#   if len(seq) == m :
#     print(*seq)
#     return
  
#   prev = None
#   for i in data :
#     if prev == i : continue
#     prev = i
#     seq.append(i)
#     permR(seq)
#     seq.pop()

# permR([])

import itertools

n,m = map(int, input().split())
data = sorted(map(int, input().split()))

result = set()
for perm in itertools.product(data, repeat=m) :
  result.add(perm)

for answer in sorted(result) :
  print(*answer)