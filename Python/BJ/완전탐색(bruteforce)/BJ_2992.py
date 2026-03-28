s = input()

lst = []
for i in range(len(s)) :
  lst.append(s[i:i+1])

n = int(s)
answer = float('inf')

from itertools import permutations

for p in permutations(lst, len(s)) :
  x = int(''.join(p))
  if x > n :
    answer = min(answer, x)

if answer == float('inf') :
  print(0)
else : 
  print(answer)