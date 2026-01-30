import sys
from collections import deque
input = sys.stdin.readline

def bfs(box, tomato_1, tomato_0) :
  q = deque(tomato_1)
  day = 0

  while q :
    day += 1
    for _ in range(len(q)) :
      z, x, y = q.popleft()
      for i in range(6) :
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and box[nz][nx][ny] == 0:
          box[nz][nx][ny] = 1
          tomato_0 -= 1
          q.append([nz, nx, ny])
    if tomato_0 == 0 :
      break

  if tomato_0 != 0 :
    print(-1)
  else :
    print(day)

m, n, h = map(int, input().split())
box = []
tomato_1 = []
tomato_all = True
tomato_0 = 0

for i in range(h) : # z
  layer = []
  for j in range(n) : # x
    row = list(map(int, input().split()))
    layer.append(row)
    for k in range(m) : # y
      if row[k] == 1 :
        tomato_1.append([i, j, k])
      if row[k] == 0 :
        tomato_0 += 1
        tomato_all = False

  box.append(layer)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

if tomato_all :
  print(0)
else :
  bfs(box, tomato_1, tomato_0)