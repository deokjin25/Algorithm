import sys
input = sys.stdin.readline
from collections import deque, defaultdict
import copy

n, m = map(int, input().split())
space = []
for i in range(n) :
  row = input()
  space.append([int(row[j]) for j in range(m)])

group_space = copy.deepcopy(space)

dr = [0,0,1,-1]
dc = [1,-1,0,0]

visited = [[0] * m for _ in range(n)]
group_cnt = defaultdict(int)

def group_zero(i,j) :
  q = deque()
  q.append((i,j))
  visited[i][j] = 1
  group_cnt[idx] += 1
  group_space[i][j] = idx
  while q :
    x, y = q.popleft()
    for k in range(4) :
      nr = x + dr[k]
      nc = y + dc[k]
      if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and space[nr][nc] == 0 :
        visited[nr][nc] = 1
        group_cnt[idx] += 1
        group_space[nr][nc] = idx
        q.append((nr,nc))

#0 그룹화
idx = 2
for i in range(n) :
  for j in range(m) :
    if group_space[i][j] == 0 :
      group_zero(i,j)
      idx+=1

#주변 경로 탐색
for i in range(n) :
  for j in range(m) :
    if space[i][j] == 1 :
      tmp = 0
      adj_group = set()
      for k in range(4) :
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < n and 0 <= nc < m and space[nr][nc] == 0 :
          adj_group.add(group_space[nr][nc])
      for group in adj_group :
        tmp += group_cnt[group]
      space[i][j] = (tmp + 1) % 10

for i in range(n) :
  for j in range(m) :
    print(space[i][j], end='')
  print()