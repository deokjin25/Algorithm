import sys
input = sys.stdin.readline
from collections import defaultdict
p = defaultdict(int)
p[1] = p[2] = p[3] = 1
p[4] = p[5] = 2

t = int(input())

def pn(n) :
  if p[n] :
    return p[n]
  p[n] = pn(n-1) + pn(n-5)
  return p[n]

for _ in range(t) :
  n = int(input())
  print(pn(n))