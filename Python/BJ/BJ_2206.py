import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
space = []
for i in range(n) :
  row = input()
  space.append([int(row[j]) for j in range(m)])

visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
dr = [0,0,1,-1]
dc = [1,-1,0,0]

q = deque()
q.append((0,0,False,1))
visited[0][0][0] = True

answer = -1
while q :
  x, y, break_wall, d = q.popleft()

  if x == n-1 and y == m-1 :
    answer = d
    break

  for i in range(4) :
    nr = x + dr[i]
    nc = y + dc[i]
    if 0 <= nr < n and 0 <= nc < m :
      if space[nr][nc] == 0 and not visited[nr][nc][int(break_wall)] :
        visited[nr][nc][int(break_wall)] = True
        q.append((nr,nc,break_wall,d+1))
      elif space[nr][nc] == 1 and not break_wall and not visited[nr][nc][1] :
        visited[nr][nc][1] = True
        q.append((nr,nc,True,d+1))

print(answer)