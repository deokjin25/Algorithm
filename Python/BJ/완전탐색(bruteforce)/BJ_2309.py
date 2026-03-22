h = []
for _ in range(9) :
  h.append(int(input()))

from itertools import combinations

for c in combinations(h, 7) :
  if sum(c) == 100 :
    c = list(c)
    c.sort()
    for i in c :
      print(i)
    break