# 인접 행렬
# from collections import deque
# import sys
# sys.setrecursionlimit(10**6)

# n, m, v = map(int, input().split())

# graph = [[0] * (n+1) for _ in range(n+1)]

# for i in range(m) :
#   a, b = map(int, input().split())
#   graph[a][b] = 1
#   graph[b][a] = 1


# def dfs(v, visited) :
#   print(v , end = ' ')
#   for i in range(1,n+1) :
#     if graph[v][i] == 0 or visited[i] == 1 : continue
#     visited[i] = 1
#     dfs(i, visited)

# def bfs(v, visited) :
#   q = deque([v])
#   visited[v] = 1

#   while q :
#     v = q.popleft()
#     print(v, end=' ')
#     for i in range(1, n+1) :
#       if graph[v][i] == 0 or visited[i] == 1 : continue
#       visited[i] = 1
#       q.append(i)

# visited = [0] * (n+1)
# visited[v] = 1
# dfs(v, visited)
# print()
# visited = [0] * (n+1)

# bfs(v, visited)

# 인접 리스트
from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

for i in range(1, n+1) :
  graph[i].sort()

def dfs(node, visited) :
  visited[node] = True
  print(node, end=' ')

  for next_node in graph[node] :
    if not visited[next_node] :
      dfs(next_node, visited)

def bfs(start, visited) :
  q = deque([start])
  visited[start] = True
  while q :
    cur = q.popleft()
    print(cur, end=' ')
    for next_node in graph[cur] :
      if not visited[next_node] :
        visited[next_node] = True
        q.append(next_node)

visited = [False] * (n+1)
dfs(v, visited)
print()

visited = [False] * (n+1)
bfs(v, visited)