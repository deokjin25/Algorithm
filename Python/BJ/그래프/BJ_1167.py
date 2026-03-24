import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    nodes = list(map(int, input().split()))
    node_a = nodes[0]
    for j in range(1, len(nodes), 2):
        node_b = nodes[j]
        if node_b == -1: break
        graph[node_a].append((node_b, nodes[j+1]))
        graph[node_b].append((node_a, nodes[j+1]))  # 양방향 추가

def bfs(start):
    visited = [-1] * (n+1)
    visited[start] = 0
    q = deque([start])
    farthest = start
    while q:
        curr = q.popleft()
        for next_node, dist in graph[curr]:
            if visited[next_node] == -1:
                visited[next_node] = visited[curr] + dist
                q.append(next_node)
                if visited[next_node] > visited[farthest]:
                    farthest = next_node
    return farthest, visited[farthest]

# 1단계: 노드 1에서 가장 먼 노드 찾기
node_a, _ = bfs(1)
# 2단계: node_a에서 가장 먼 노드 찾기
node_b, diameter = bfs(node_a)
print(diameter)