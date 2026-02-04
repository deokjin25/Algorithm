import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
answer = []

for _ in range(n) :
  x = int(input())
  if x == 0 :
    if len(q) == 0 :
      answer.append(str(0))
    else :
      answer.append(str(-heapq.heappop(q)))
  else :
    heapq.heappush(q, -x)

print(('\n').join(answer))
