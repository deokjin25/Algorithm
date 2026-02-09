# import heapq

# n = int(input())
# q = []
# for _ in range(n) :
#   heapq.heappush(q, tuple(map(int, input().split())))

# room = [[heapq.heappop(q)]]
# while q :
#   start, end = heapq.heappop(q)

#   flag = True
#   for i in range(len(room)) :
#     roomEnd = room[i][-1][1]
#     if start >= roomEnd :
#       room[i].append((start, end))
#       flag = False
#       break
  
#   if flag : 
#     room.append([(start,end)])

# print(len(room))

# 필요한건 오직 회의실 개수 (회의실의 회의 구성이 아님)
import heapq
import sys
input = sys.stdin.readline

n = int(input())
mettings = []
for _ in range(n) :
  s, e = map(int, input().split())
  mettings.append((s,e))

mettings.sort()

room = []

for start, end in mettings :
  if room and room[0] <= start :
    heapq.heappop(room)
  heapq.heappush(room, end)

print(len(room))