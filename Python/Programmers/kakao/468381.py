#왼, 오, 아래, 위
track_connect = {
  1 : [[1, 3, 5, 6], [1, 3, 4, 7], [], []],
  2 : [[], [], [2, 3, 4, 5], [2, 3, 6, 7]],
  3 : [[1, 3, 5, 6], [1, 3, 4, 7], [2, 3, 4, 5], [2, 3, 6, 7]],
  4 : [[1, 3, 5, 6], [], [], [2, 3, 6, 7]],
  5 : [[], [1, 3, 4, 7], [], [2, 3, 6, 7]],
  6 : [[], [1, 3, 4, 7], [2, 3, 4, 5], []],
  7 : [[1, 3, 5, 6], [], [2, 3, 4, 5], []]  
}

dr = [0,0,1,-1]
dc = [-1,1,0,0]
answer = 0

def switch_direction(d, track) :
    if track in [1, 2, 3] :
        return d

    if (d == 1 and track == 4) or (d == 0 and track == 5) :
        return 3
    if (d == 0 and track == 6) or (d == 1 and track == 7) :
        return 2
    if (d == 2 and track == 4) or (d == 3 and track == 7) :
        return 0
    if (d == 2 and track == 5) or (d == 3 and track == 6) :
        return 1
    
def track_3(grid, n, m) :
    for i in range(n) :
        for j in range(m) :
            if grid[i][j] == 3 :
                for k in range(4) :
                    nr = i + dr[k]
                    nc = j + dc[k]

                    if nr<0 or nr>=n or nc<0 or nc>=m :
                        return False
                    
                    if grid[nr][nc] <= 0 :
                        return False
                    if grid[nr][nc] not in track_connect[3][k] :
                        return False
    return True

def dfs(grid, track, d, r, c, n, m, exist) :
    global answer

    if r == n-1 and c == m-1 :
        if len(exist) == 0 and track_3(grid, n, m) :
        #   for i in range(n) :
        #       print(grid[i])
        #   print()
          answer += 1
        return
    
    #연결 가능한 선로
    can_connect_track = track_connect[track][d]

    nr = r + dr[d]
    nc = c + dc[d]

    if nr < 0 or nr >= n or nc < 0 or nc >= m :
        return

    #빈 땅이 아닌 경우
    if grid[nr][nc] != 0 :
        if grid[nr][nc] == -1 or grid[nr][nc] not in can_connect_track:
            return
        else :
            next_d = switch_direction(d, grid[nr][nc])
            tmp = False
            if (nr, nc) in exist :
                exist.remove((nr,nc))
                tmp = True
            dfs(grid, grid[nr][nc], next_d, nr, nc, n, m, exist)
            if tmp :
                exist.add((nr, nc))
    else :
        #빈 땅인 경우
        for tmp_track in can_connect_track :
            grid[nr][nc] = tmp_track
            next_d = switch_direction(d, grid[nr][nc])
            dfs(grid, grid[nr][nc], next_d, nr, nc, n, m, exist)
            grid[nr][nc] = 0

def solution(grid):
    global answer
    n, m = len(grid), len(grid[0])

    exist = set()
    for i in range(n) :
        for j in range(m) :
            if (i==0 and j == 0) or (i == n-1 and j == m-1) :
                continue
            if grid[i][j] > 0 :
                exist.add((i,j))
    dfs(grid, 1, 1, 0, 0, n, m, exist)
    
    return answer

# print(solution([[1, 0, 0, 0, 0], [0, 0, 3, 0, 2], [0, 0, 0, 0, 2]]))