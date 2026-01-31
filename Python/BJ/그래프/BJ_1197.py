# Kruskal
import sys
sys.setrecursionlimit(10**6)
v, e = map(int, input().split())

edges = []
for _ in range(e):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

# 가중치 기준 정렬
edges.sort()

# Union-Find
parent = list(range(v + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

answer = 0
edge_count = 0

for w, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += w
        edge_count += 1
        if edge_count == v - 1:
            break

print(answer)

# Prim
# import heapq

# v, e = map(int, input().split())

# # 양방향 그래프로 저장
# graph = [[] for _ in range(v + 1)]
# for _ in range(e):
#     a, b, w = map(int, input().split())
#     graph[a].append((w, b))
#     graph[b].append((w, a))

# # Prim 알고리즘
# visited = [False] * (v + 1)
# min_heap = [(0, 1)]  # (가중치, 정점) - 1번 정점에서 시작
# answer = 0
# edge_count = 0

# while min_heap and edge_count < v:
#     weight, node = heapq.heappop(min_heap)
    
#     # 이미 방문한 정점은 스킵
#     if visited[node]:
#         continue
    
#     # 방문 처리 및 가중치 추가
#     visited[node] = True
#     answer += weight
#     edge_count += 1
    
#     # 현재 정점과 연결된 간선들을 힙에 추가
#     for next_weight, next_node in graph[node]:
#         if not visited[next_node]:
#             heapq.heappush(min_heap, (next_weight, next_node))

# print(answer)