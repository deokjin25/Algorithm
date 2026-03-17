# import sys
# input = sys.stdin.readline
# from collections import deque

# n,m,x = map(int, input().split())

# graph = [[] for _ in range(n+1)]

# for _ in range(m) :
#   s, e, t = map(int, input().split())
#   graph[s].append((e,t))

# def dijkstra(node) :
#   distance = [float('inf')] * (n+1)
#   q = deque()

#   for e, t in graph[node] :
#     q.append((e,t))
#     distance[e] = t

#   while q :
#     e, total = q.popleft()

#     for next_node, time in graph[e] :
#       if total + time < distance[next_node] :
#         distance[next_node] = total + time
#         q.append((next_node, total+time))

#   return distance

# distance_all = [[]]
# for i in range(1,n+1) :
#   distance_all.append(dijkstra(i))

# # print(distance_all)

# answer = 0
# for i in range(1,n+1) :
#   d = distance_all[i][x] + distance_all[x][i]
#   if i == x :
#     d = d // 2
#   answer = max(answer, d)
# print(answer)

import sys
input = sys.stdin.readline
import heapq

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def dijkstra(node):
    distance = [float('inf')] * (n+1)
    distance[node] = 0
    pq = [(0, node)]

    while pq:
        total, cur = heapq.heappop(pq)

        if total > distance[cur]:
            continue

        for next_node, time in graph[cur]:
            new_cost = total + time
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return distance

distance_all = [None] + [dijkstra(i) for i in range(1, n+1)]

answer = 0
for i in range(1, n+1):
    d = distance_all[i][x] + distance_all[x][i]
    answer = max(answer, d)

print(answer)