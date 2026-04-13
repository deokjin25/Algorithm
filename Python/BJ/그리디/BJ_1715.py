import heapq
import sys
input = sys.stdin.readline
n = int(input())

if n == 1 :
  print(0)
else :
  cards = []
  for _ in range(n) :
    heapq.heappush(cards, int(input()))

  cnt = 0
  while True :
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    cnt += a+b
    heapq.heappush(cards, a+b)

    if len(cards) == 1 :
      break

  print(cnt)