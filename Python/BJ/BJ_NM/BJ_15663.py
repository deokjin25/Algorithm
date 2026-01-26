# n, m = map(int, input().split())
# data = sorted(map(int, input().split()))

# def perm(visited, seq:list) :
#   if len(seq) == m:
#     print(*seq)
#     return
  
#   prev = None
#   for idx, val in enumerate(data) :
#     if visited[idx] or prev == val : continue
#     prev = val
#     visited[idx] = True
#     seq.append(val)
#     perm(visited, seq)
#     seq.pop()
#     visited[idx] = False

# perm([False]*n, [])

from itertools import permutations

n, m = map(int, input().split())
data = sorted(map(int, input().split()))

result = set()
for perm in permutations(data, m):
    result.add(perm)

for perm in sorted(result):
    print(*perm)