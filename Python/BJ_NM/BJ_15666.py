# n,m = map(int, input().split())
# data = sorted(map(int, input().split()))

# def combR(seq, idx) :
#   if len(seq) == m :
#     print(*seq)
#     return
  
#   prev = None
#   for i in range(idx, n) :
#     if prev == data[i] : continue
#     prev = data[i]
#     seq.append(data[i])
#     combR(seq, i)
#     seq.pop()

# combR([],0)

import itertools

n,m = map(int, input().split())
data = sorted(map(int, input().split()))

result = set()
for comb in itertools.combinations_with_replacement(data, m) :
  result.add(comb)

for answer in sorted(result) :
  print(*answer)