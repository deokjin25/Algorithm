import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

count = [0] * (n+1)
graph= [[] for _ in range(n+1)]
for _ in range(m) :
  singer_list = list(map(int, input().split()))
  for i in range(1, singer_list[0]) :
    graph[singer_list[i]].append(singer_list[i+1])
    count[singer_list[i+1]] += 1

q= deque()
for i in range(1, n+1) :
  if count[i] == 0 :
    q.append(i)

answer = []
while q :
  singer = q.popleft()
  answer.append(str(singer))
  for next_singer in graph[singer] :
    count[next_singer] -= 1
    if count[next_singer] == 0 :
      q.append(next_singer)

if len(answer) == n :
  print(('\n').join(answer))
else :
  print(0)