import sys
input = sys.stdin.readline

n = int(input())
board = [input().rstrip() for _ in range(n)]

w_min = n
w_max = 0
h_min = n
h_max = 0

for i in range(n) :
  for j in range(n) :
    if board[i][j] == 'G' :
      w_min = min(j, w_min)
      w_max = max(j, w_max)

      if h_min == n :
        h_min = i
        continue
      
      h_max = i

#G가 하나인 경우
if w_min == w_max and h_min == h_max :
  print(0)
#가로에만 배치된 경우
elif h_min == h_max :
  print(w_max - w_min + min(w_min, n-1-w_max))
#세로에만 배치된 경우
elif w_min == w_max :
  print(h_max - h_min + min(h_min, n-1-h_max))
#가로 세로 흩어진 경우
else :
  print(w_max - w_min + min(w_min, n-1-w_max) +
        h_max - h_min + min(h_min, n-1-h_max))