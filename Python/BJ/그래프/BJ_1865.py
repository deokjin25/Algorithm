def bellman_ford(N, edges):
    dist = [0] * (N + 1)
    
    for _ in range(N - 1):
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    
    for u, v, w in edges:
        if dist[v] > dist[u] + w:
            return 'YES'  # 음수 사이클 있음
    
    return 'NO'

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    n, m, w = map(int, input().split())

    edges = []
    for _ in range(m) :
        s, e, t = map(int, input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))

    for _ in range(w) :
        s, e, t = map(int, input().split())
        edges.append((s,e,-t))

    print(bellman_ford(n,edges))