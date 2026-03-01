# import sys
# input = sys.stdin.readline
# from collections import deque

# n,m = map(int, input().split())

# graph = [[] for _ in range(n+1)]
# priority = [0] * (n+1)
# starting = [0] * (n+1)

# for _ in range(m) :
#   s, e = map(int, input().split())
#   graph[s].append(e)
#   priority[e] += 1

# x = int(input())

# q = deque()

# for i in range(1, n+1) :
#   if priority[i] == 0 :
#     q.append((i,0))

# answer = 0
# while q :
#   node, job = q.popleft()

#   if node == x :
#     print(job)
#     break

#   for next_node in graph[node] :
#     priority[next_node] -= 1

#     if priority[next_node] == 0 :
#       q.append((next_node, job+1))

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    reverse_graph[e].append(s)

x = int(input())

visited = [False] * (n + 1)
q = deque()
q.append(x)
visited[x] = True

answer = 0
while q:
    node = q.popleft()
    for prev_node in reverse_graph[node]:
        if not visited[prev_node]:
            visited[prev_node] = True
            answer += 1
            q.append(prev_node)

print(answer)