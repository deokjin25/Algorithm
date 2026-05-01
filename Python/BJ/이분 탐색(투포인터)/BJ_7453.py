import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
lst_a = []
lst_b = []
lst_c = []
lst_d = []

for _ in range(n) :
  a, b, c, d = map(int, input().split())
  lst_a.append(a)
  lst_b.append(b)
  lst_c.append(c)
  lst_d.append(d)

ab_count = defaultdict(int)
for a in lst_a :
  for b in lst_b :
    ab_count[a+b] += 1

# cd_count = defaultdict(int)
# for c in lst_c :
#   for d in lst_d :
#     cd_count[c+d] += 1

answer=0
for c in lst_c :
  for d in lst_d :
    target = -(c+d)
    if target in ab_count :
      answer += ab_count[target]

print(answer)