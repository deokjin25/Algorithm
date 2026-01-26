# from collections import deque
import heapq
import copy
import sys
input = sys.stdin.readline

def bfs(lab, visit, select_virus_index) :
    q = []

    for i in select_virus_index :
        x,y = virus_positions[i]
        lab[x][y] = 0
        heapq.heappush(q, (0,x,y)) 
        visit[x][y] = 1

    while q :
        t, x, y = heapq.heappop(q)

        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)) :
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n : continue #범위 벗어나면 pass
            if visit[nx][ny] == 0 and (lab[nx][ny] == 0 or lab[nx][ny] == 2) :
                visit[nx][ny] = 1
                lab[nx][ny] = t+1
                heapq.heappush(q, (t+1, nx, ny))
    return lab

def simulation(lab, select_virus_index) :
    global flag
    #방문 배열 생성
    visit = [[0]*n for _ in range(n)]

    #바이러스 살포
    lab = bfs(lab,visit,select_virus_index)

    #최대 시간 count
    max_t = 0
    for i in range(n) :
        for j in range(n) :
            if lab[i][j] == 0 and visit[i][j] == 0 : return 10e9    #퍼트리지 못한 경우
            if visit[i][j] == 0 and lab[i][j] == 1 : continue #벽인 경우 pass
            max_t = max(lab[i][j], max_t)
    flag = True
    return max_t

def select_virus(index, s) :
    global virus_positions
    global answer
    if s == m :
        #시뮬레이션 전용 맵 생성
        simulation_lab = copy.deepcopy(init_lab)

        #선택된 바이러스만 남김
        for i in range(0, len(virus_positions)) :
            if i not in select_virus_index :
                x, y = virus_positions[i]
                simulation_lab[x][y] = 0

        #시뮬레이션 시작     
        answer = min(answer, simulation(simulation_lab, select_virus_index))

        return
    
    #바이러스 위치 조합 생성
    for i in range(index, len(virus_positions)) :
        select_virus_index.append(i)
        select_virus(i+1, s+1)
        select_virus_index.pop()


n, m = map(int, input().split())

#초기 맵
init_lab = [list(map(int, input().split())) for _ in range(n)]

#바이러스 위치 list
virus_positions = []

#선택한 바이러스 위치 list
select_virus_index = []

for i in range(n) :
    for j in range(n) :
        if init_lab[i][j] == 2 :
            virus_positions.append((i,j))

flag = False #한번도 바이러스 살포에 성공한 적이 없었는지 확인할 변수
answer = 10e9
select_virus(0, 0)

if flag :
    print(answer)
else :
    print(-1)


