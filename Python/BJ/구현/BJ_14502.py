from collections import deque
import copy
import sys
input = sys.stdin.readline

def bfs(x, y, lab, visit) :
    q = deque()
    q.append((x,y))
    visit[x][y] = 1

    while q :
        x,y = q.popleft()

        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)) :
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m : continue
            if visit[nx][ny] == 1 or lab[nx][ny] != 0: continue
            visit[nx][ny] = 1
            lab[nx][ny] = 2
            q.append((nx,ny))
    return

def simulation(lab) :
    #방문 배열 생성
    visit = [[0]*m for _ in range(n)]

    #바이러스 살포
    for i in range(n) :
        for j in range(m) :
            if visit[i][j] == 1 or lab[i][j] != 2: continue
            bfs(i,j,lab,visit)

    #안전 구역 count
    clear_area = 0
    for i in range(n) :
        for j in range(m) :
            if lab[i][j] == 0 :
                clear_area += 1

    return clear_area

def select_wall_index(index, s) :
    global answer
    if s == 3 :
        #시뮬레이션 전용 맵 생성
        simulation_map = copy.deepcopy(init_map)

        #선택된 3개의 벽 인덱스에 대해 벽 생성
        for x,y in select_walls :
            simulation_map[x][y] = 1

        #시뮬레이션 시작        
        answer = max(answer, simulation(simulation_map))

        return
    
    for i in range(index, n*m) :
        if init_map[i//m][i%m] != 0 : continue   #이미 벽이면 pass
        select_walls.append((i//m, i%m))
        select_wall_index(i+1, s+1)
        select_walls.pop()


n, m = map(int, input().split())

# init_map = [ for _ in range(n) list(map(int, input().split())]
init_map = []

#세울 벽 list
select_walls = []

for _ in range(n) :
    init_map.append(list(map(int, input().split())))

answer = 0
select_wall_index(0,0)
print(answer)