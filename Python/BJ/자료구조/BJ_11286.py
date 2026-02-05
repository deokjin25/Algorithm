import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
answer = []

for _ in range(n) :
  x = int(input())
  if x == 0 :
    if len(q) == 0 :
      answer.append('0')
    else : 
      abs_num, is_positive = heapq.heappop(q)
      answer.append(str(abs_num) if is_positive else str(-abs_num))
  elif x > 0 :
    heapq.heappush(q, (x, True))
  else :
    heapq.heappush(q, (-x, False))

print(('\n').join(answer))