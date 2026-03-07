import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
answer = []
for _ in range(T) :
  n, x = map(int, input().split())
  priorities = list(map(int, input().split()))
  for i in range(n) :
    p = priorities[i]
    priorities[i] = [p,i]

  priorities = deque(priorities)
  cnt = 0
  while priorities :
    high_order = max(x[0] for x in priorities)
    p, idx = priorities.popleft()

    if p == high_order and idx == x :
      answer.append(str(cnt+1))
      break
    
    elif p == high_order :
      cnt+=1

    else :
      priorities.append([p,idx])

print(('\n').join(answer))