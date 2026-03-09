# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n,m = map(int, input().split())
# space = [ list(map(int, input().split())) for _ in range(n) ]

# #dp[x][y][d]: x, y 지점에서 d 방향으로 갔을 때의 경로 개수
# dp = [[[0]*4 for _ in range(m)] for _ in range(n)]

# dr = [0,0,-1,1]
# dc = [1,-1,0,0]

# visited = [[0] * m for _ in range(n)]
# cal_dp = [[0] * m for _ in range(n)]

# def dp_dfs(rx, ry, cur) :
#   #dp를 계산한 곳이면 dp값을 return
#   if cal_dp[rx][ry] :
#     return sum(dp[rx][ry])

#   #목적지 도착
#   if rx == n-1 and ry == m-1 :
#     return 1

#   #dp 계산 표시
#   cal_dp[rx][ry] = 1

#   for i in range(4) :
#     nr = dr[i] + rx
#     nc = dc[i] + ry
#     if 0<=nr<n and 0<=nc<m and not visited[nr][nc] :
#       #내리막길 여부
#       if space[nr][nc] < cur :
#         visited[nr][nc] = 1
#         dp[rx][ry][i] = dp_dfs(nr, nc, space[nr][nc])
#         visited[nr][nc] = 0

#   return sum(dp[rx][ry])

# dp_dfs(0,0,space[0][0])

# print(sum(dp[0][0]))

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dr[i], y + dc[i]
        if 0 <= nx < n and 0 <= ny < m and space[nx][ny] < space[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))