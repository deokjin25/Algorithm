import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())

dr = [-1,1,0,0]
dc = [0,0,-1,1]
match_d = {0:'U', 1:'D', 2:'L', 3:'R'}

board = []
for i in range(n) :
  row = list(input().strip())
  board.append(row)
  for j in range(m) :
    if row[j] == 'R' :
      rr, rc = i, j
    elif row[j] == 'B' :
      br, bc = i, j

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def move_one(board, r, c, d):
    while True:
        r += dr[d]
        c += dc[d]
        if board[r][c] == '#':
            r -= dr[d]
            c -= dc[d]
            return r, c, False
        if board[r][c] == 'O':
            return r, c, True

def move(board, rr, rc, br, bc, d):
    # 1. 빨간, 파란 각각 굴리기
    nrr, nrc, red_in = move_one(board, rr, rc, d)
    nbr, nbc, blue_in = move_one(board, br, bc, d)

    # 2. 둘 다 구멍에 안 빠졌고 같은 칸이면 조정
    if not red_in and not blue_in and nrr == nbr and nrc == nbc:
        # 원래 더 앞에 있던 구슬을 한 칸 뒤로
        if d == 0 and rr > br: nrr += 1
        elif d == 0 and rr < br: nbr += 1
        elif d == 1 and rr < br: nrr -= 1
        elif d == 1 and rr > br: nbr -= 1
        elif d == 2 and rc > bc: nrc += 1
        elif d == 2 and rc < bc: nbc += 1
        elif d == 3 and rc < bc: nrc -= 1
        elif d == 3 and rc > bc: nbc -= 1

    return nrr, nrc, nbr, nbc, red_in, blue_in

def solve(rr, rc, br, bc):
    q = deque()
    q.append((rr, rc, br, bc, 0, ''))
    visited[rr][rc][br][bc] = True

    while q:
        rr, rc, br, bc, cnt, directions = q.popleft()
        if cnt == 10: continue

        for d in range(4):
            nrr, nrc, nbr, nbc, red_in, blue_in = move(board, rr, rc, br, bc, d)
            if blue_in: continue
            if red_in: 
               return [cnt+1, directions + match_d[d]]
            if not visited[nrr][nrc][nbr][nbc]:
                visited[nrr][nrc][nbr][nbc] = True
                q.append((nrr, nrc, nbr, nbc, cnt+1, directions + match_d[d]))
    return -1

answer = solve(rr, rc, br, bc)
if answer == -1 :
   print(-1)
else :
   print(answer[0])
   print(answer[1])