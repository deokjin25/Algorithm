import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
space = [input().strip() for _ in range(n)]

visited = [[[[0] * m for _ in range(n)] for _ in range(k+1)] for _ in range(2)]
dr = [0,0,1,-1]
dc = [1,-1,0,0]

q = deque()
q.append((0,0,0,1))
visited[1][0][0][0] = 1

answer = -1
while q :
  x, y, wall_count, d = q.popleft()

  if x == n-1 and y == m-1 :
    answer = d
    break

  is_day = d % 2
  next_time = 1 - is_day

  for i in range(4) :
    nr = x + dr[i]
    nc = y + dc[i]
    if 0 <= nr < n and 0 <= nc < m :
      if space[nr][nc] == '0' and not visited[next_time][wall_count][nr][nc] :
        visited[next_time][wall_count][nr][nc] = 1
        q.append((nr,nc,wall_count,d+1))
      elif space[nr][nc] == '1' and wall_count < k :
        if is_day == 1 :
          if not visited[next_time][wall_count][nr][nc] :
            visited[next_time][wall_count][nr][nc] = 1
            q.append((nr,nc,wall_count+1,d+1))
        else :
          if not visited[next_time][wall_count][nr][nc] :
            visited[next_time][wall_count][nr][nc] = 1
            q.append((x,y,wall_count,d+1))

print(answer)