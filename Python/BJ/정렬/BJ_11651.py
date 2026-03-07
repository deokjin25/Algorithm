# import sys
# input = sys.stdin.readline

# n = int(input())
# lst = []
# for _ in range(n) :
#   x, y = map(int, input().split())
#   lst.append((x,y))

# lst.sort(key= lambda x: (x[1], x[0]))

# for i in range(n) :
#   print(*lst[i])

import sys
input = sys.stdin.readline
import heapq

n = int(input())
hq = []
for _ in range(n) :
  x, y = map(int, input().split())
  heapq.heappush(hq, (y,x))

for i in range(n) :
  y, x = heapq.heappop(hq)
  print(x, y)