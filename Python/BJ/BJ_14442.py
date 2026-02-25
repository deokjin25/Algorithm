import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
space = [input().strip() for _ in range(n)]

visited = [[[False] * (m) for _ in range(n)] for _ in range(k+1)]
dr = [0,0,1,-1]
dc = [1,-1,0,0]

q = deque()
q.append((0,0,0,1))
visited[0][0][0] = True

answer = -1
while q :
  x, y, wall_count, d = q.popleft()

  if x == n-1 and y == m-1 :
    answer = d
    break

  for i in range(4) :
    nr = x + dr[i]
    nc = y + dc[i]
    if 0 <= nr < n and 0 <= nc < m :
      if space[nr][nc] == '0' and not visited[wall_count][nr][nc] :
        visited[wall_count][nr][nc] = True
        q.append((nr,nc,wall_count,d+1))
      elif space[nr][nc] == '1' and wall_count < k and not visited[wall_count+1][nr][nc] :
        visited[wall_count+1][nr][nc] = True
        q.append((nr,nc,wall_count+1,d+1))

print(answer)