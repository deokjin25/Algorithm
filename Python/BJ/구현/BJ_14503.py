# d - 0: 북, 1: 동, 2: 남, 3: 서
# room[r][c] - 0: 청소되지 않은 빈칸, 1: 벽
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(n) :
  row = list(map(int, input().split()))
  room.append(row)

dr = [-1,1,0,0]
dc = [0,0,1,-1]

class robot :
  def __init__(self, r, c, d) :
    self.r = r
    self.c = c
    self.d = d
    room[r][c] = 2
    self.clean = 1

  def rotate(self) :
    self.d = (self.d - 1) % 4

  def stop(self) :
    print(self.clean)

  def clean_ok(self) :
    for i in range(4) :
      nr = self.r + dr[i]
      nc = self.c + dc[i]
      if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0 :
        return True
    return False
  
  def do_clean(self) :
    if self.d == 0 and self.r-1 >=0 and room[self.r-1][self.c] == 0 :
      self.r -= 1
      self.clean += 1
    if self.d == 1 and self.c+1 < m and room[self.r][self.c+1] == 0 :
      self.c += 1
      self.clean += 1
    if self.d == 2 and self.r+1 < n and room[self.r+1][self.c] == 0 :
      self.r += 1
      self.clean += 1
    if self.d == 3 and self.c-1 >= 0 and room[self.r][self.c-1] == 0 :
      self.c -= 1
      self.clean += 1

  def go_back(self) :
    if self.d == 0 and self.r+1 < n and room[self.r+1][self.c] != 1 :
      self.r += 1
      return True
    if self.d == 1 and self.c-1 >= 0 and room[self.r][self.c-1] != 1 :
      self.c -= 1
      return True
    if self.d == 2 and self.r-1 >= 0 and room[self.r-1][self.c] != 1 :
      self.r -= 1
      return True
    if self.d == 3 and self.c+1 < m and room[self.r][self.c+1] != 1 :
      self.c += 1
      return True
    return False

  def start(self) :
    while True :
      if self.clean_ok() :
        self.rotate()
        self.do_clean()
        room[self.r][self.c] = 2
      else :
        if self.go_back() :
          continue
        else :
          self.stop()
          return

robot = robot(r, c, d)
robot.start()