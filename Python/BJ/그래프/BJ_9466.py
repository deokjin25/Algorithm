# import sys
# input = sys.stdin.read
# data = input().split()

# index = 0
# T = int(data[index])
# index += 1

# for _ in range(T):
#     n = int(data[index])
#     index += 1
#     vote = [0] + [int(x) for x in data[index:index+n]]
#     index += n
    
#     visited = [0] * (n+1)  # 0: 미방문, 1: 방문 중, 2: 완료
#     team = [False] * (n+1)  # 팀에 속하는지
    
#     def dfs(node):
#         stack = []
#         path = []
#         stack.append(node)
#         while stack:
#             current = stack[-1]
#             if visited[current] == 0:
#                 visited[current] = 1
#                 path.append(current)
#                 next_node = vote[current]
#                 if visited[next_node] == 0:
#                     stack.append(next_node)
#                 elif visited[next_node] == 1:  # 사이클 발견
#                     idx = path.index(next_node)
#                     for i in range(idx, len(path)):
#                         team[path[i]] = True
#                     return
#             else:
#                 visited[current] = 2
#                 path.pop()
#                 stack.pop()
    
#     for i in range(1, n+1):
#         if visited[i] == 0:
#             dfs(i)
    
#     no_team = sum(1 for i in range(1, n+1) if not team[i])
#     print(no_team)

# import sys
# input = sys.stdin.read
# data = input().split()

# index = 0
# T = int(data[index])
# index += 1

# for _ in range(T):
#     n = int(data[index])
#     index += 1
#     vote = [0] + [int(x) for x in data[index:index+n]]
#     index += n
    
#     parent = list(range(n+1))
#     rank = [0] * (n+1)
#     team = [False] * (n+1)  # 팀에 속하는 노드
    
#     def find(x):
#         if parent[x] != x:
#             parent[x] = find(parent[x])  # 경로 압축
#         return parent[x]
    
#     def union(x, y):
#         px, py = find(x), find(y)
#         if px == py:
#             return False  # 이미 같은 그룹 (사이클 가능)
#         if rank[px] < rank[py]:
#             parent[px] = py
#         elif rank[px] > rank[py]:
#             parent[py] = px
#         else:
#             parent[py] = px
#             rank[px] += 1
#         return True
    
#     # 각 노드에 대해 union 수행
#     for i in range(1, n+1):
#         next_node = vote[i]
#         if not union(i, next_node):
#             # union 실패: 사이클 감지, 현재 경로의 노드들을 팀으로 설정
#             # 하지만 Union-Find로는 정확한 사이클 노드를 추적하기 어려움
#             # 간단히, 투표 방향으로 따라가며 사이클 노드 찾기
#             visited = set()
#             current = i
#             while current not in visited:
#                 visited.add(current)
#                 current = vote[current]
#                 if current == i:  # 사이클 발견
#                     for node in visited:
#                         team[node] = True
#                     break
    
#     # 팀 불가능한 학생 수 계산
#     no_team = sum(1 for i in range(1, n+1) if not team[i])
#     print(no_team)

import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        li = [0] + list(map(int, input().split()))
        d = [0] * (n + 1)

        for i in li:
            d[i] += 1
        
        left = [i for i in range(1, n + 1) if not d[i]]

        for i in left:
            d[li[i]] -= 1
            if not d[li[i]]:
                left.append(li[i])

        print(len(left))

if __name__ == "__main__":
    sys.setrecursionlimit(10000000)
    main()