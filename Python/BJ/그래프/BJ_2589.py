from collections import deque

n, m = map(int, input().split())
data = []
for _ in range(n) :
  row = input()
  data.append(row)

dr = [-1,1,0,0]
dc = [0,0,1,-1]

def bfs(sr, sc):
    visited = [[0]*m for _ in range(n)]
    queue = deque([(sr, sc, 0)])
    visited[sr][sc] = 1
    max_dist = 0
    
    while queue:
        r, c, dist = queue.popleft()
        max_dist = max(max_dist, dist)
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0<=nr<n and 0<=nc<m and data[nr][nc]=='L' and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc, dist+1))
    
    return max_dist

answer = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 'L':
            answer = max(answer, bfs(i, j))
print(answer)