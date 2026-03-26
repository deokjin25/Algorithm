N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):      #중간
    for i in range(N):      #출발
        for j in range(N):      #도착
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for lst in graph:
    print(*lst)