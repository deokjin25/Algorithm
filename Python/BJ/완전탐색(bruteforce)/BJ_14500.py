import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
num_board = [ list(map(int, input().split())) for _ in range(n) ]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
max_board = max(max(row) for row in num_board)
visited = [[0] * m for _ in range(n)]

def tetromino(x, y, total, tet, shape) :
  global answer

  if total + (max_board * (4 - tet)) <= answer :
    return 0

  if tet == 4 :
    return total
  
  s = 0
  if tet == 3 :
    for sx, sy in shape :
      for i in range(4) :
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] :
          visited[nx][ny] = 1
          shape.append((nx,ny))
          s = max(s, tetromino(nx, ny, total+num_board[nx][ny], tet+1, shape))
          shape.pop()
          visited[nx][ny] = 0
  else :
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m and not visited[nx][ny] :
        visited[nx][ny] = 1
        shape.append((nx,ny))
        s = max(s, tetromino(nx, ny, total+num_board[nx][ny], tet+1, shape))
        shape.pop()
        visited[nx][ny] = 0
  
  return s

answer = 0
for i in range(n) :
  for j in range(m) :
    visited[i][j] = 1
    answer = max(answer, tetromino(i, j, num_board[i][j], 1, [(i,j)]))
    visited[i][j] = 0

print(answer)