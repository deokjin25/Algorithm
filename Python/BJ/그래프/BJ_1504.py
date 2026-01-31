import heapq

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e) :
  from_, to, w = map(int, input().split())
  graph[from_].append((w, to))
  graph[to].append((w, from_))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    q = [(0, start)]
    
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        
        if cur_dist > distance[cur_node]:
            continue
        
        for weight, next_node in graph[cur_node]:
            new_dist = cur_dist + weight
            
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))
    
    return distance

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

way_1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
way_2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

INF = float('inf')
result = min(way_1, way_2)
print(result if result < INF else -1)