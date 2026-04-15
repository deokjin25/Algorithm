import heapq
import sys
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n) :
  s, e = map(int, input().split())
  classes.append((s,e))

classes.sort()

room = []
for s, e in classes :
  if room and room[0] <= s :
    heapq.heappop(room)
  heapq.heappush(room, e)

print(len(room))