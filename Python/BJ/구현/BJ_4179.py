import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
miro = [ list(input().strip()) for _ in range(r) ]
jihun = deque()
fire = deque()


j_visited = [[0]*c for _ in range(r)]
f_visited = [[0]*c for _ in range(r)]
for i in range(r) :
  for j in range(c) :
    if miro[i][j] == 'J' :
      j_visited[i][j] = 1
      jihun.append((i,j,0))
    
    if miro[i][j] == 'F' :
      f_visited[i][j] = 1
      fire.append((i,j,0))


def jihun_move(time) :

  while jihun :
    jx, jy, cur_t = jihun.popleft()

    #불타서 사라진 경우
    if miro[jx][jy] =='F' :
      continue
    
    #현재 이동시간 초과
    if cur_t > time :
      jihun.appendleft((jx, jy, cur_t))
      return False, 1

    for i in range(4) :
      nr = jx + dx[i]
      nc = jy + dy[i]

      #탈출
      if nr < 0 or nr >= r or nc < 0 or nc >= c :
        return True, cur_t+1

      if miro[nr][nc] == '.' and not j_visited[nr][nc] :
        j_visited[nr][nc] = 1
        miro[nr][nc] = 'J'
        jihun.append((nr, nc, cur_t+1))

  #이동할 수 있는 경우가 없을 때
  return False, 0

def fire_move(time) :
  while fire :
    fx, fy, cur_t = fire.popleft()

    if cur_t > time :
      fire.appendleft((fx, fy, cur_t))
      return
    
    for i in range(4) :
      nr = fx + dx[i]
      nc = fy + dy[i]
      if 0<=nr<r and 0<=nc<c and not f_visited[nr][nc] and miro[nr][nc] != '#' :
        f_visited[nr][nc] = 1
        miro[nr][nc] = 'F'
        fire.append((nr, nc, cur_t+1))

time = 0
while True :
  
  success, possible = jihun_move(time)
  if success :
    print(possible)
    break
  else :
    if not possible :
      print('IMPOSSIBLE')
      break
  fire_move(time)

  time+=1