# import sys
# input = sys.stdin.readline
# import heapq

# t = int(input())
# answer = []
# for _ in range(t) :
#   n, k = map(int, input().split())
#   build_times = list(map(int, input().split()))
#   count = [0] * (n+1)
#   graph = [[] for _ in range(n+1)]

#   for _ in range(k) :
#     before, after = map(int, input().split())
#     graph[before].append(after)
#     count[after] += 1
  
#   target = int(input())

#   q = []

#   for i in range(1,n+1) :
#     if count[i] == 0 :
#       heapq.heappush(q, (build_times[i-1], 0, i))

#   total_build_time = [0] * (n+1)
#   while q :
#     build_time, depth, building = heapq.heappop(q)

#     if len(graph[building]) == 0 and building != target :
#       continue

#     total_build_time[depth] = max(total_build_time[depth], build_time)

#     if building == target :
#       answer.append(str(sum(total_build_time[:depth+1])))
#       break

#     for to in graph[building] :
#       count[to] -= 1
#       if count[to] == 0:
#         heapq.heappush(q, (build_times[to-1], depth+1, to))

# print(('\n').join(answer))


import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
answer = []
for _ in range(t):
    n, k = map(int, input().split())
    build_times = [0] + list(map(int, input().split()))
    count = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for _ in range(k):
        before, after = map(int, input().split())
        graph[before].append(after)
        count[after] += 1
    
    target = int(input())
    
    total_time = [0] * (n+1)
    q = deque()
    
    for i in range(1, n+1):
        if count[i] == 0:
            q.append(i)
            total_time[i] = build_times[i]
    
    while q:
        building = q.popleft()
        
        for next_building in graph[building]:
            total_time[next_building] = max(total_time[next_building], 
                                            total_time[building] + build_times[next_building])
            count[next_building] -= 1
            
            if count[next_building] == 0:
                q.append(next_building)
    
    answer.append(str(total_time[target]))

print('\n'.join(answer))