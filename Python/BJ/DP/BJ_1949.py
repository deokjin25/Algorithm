# import sys
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     people = [0] + list(map(int, input().split()))

#     graph = [[] for _ in range(n+1)]
#     for _ in range(n-1):
#         s, e = map(int, input().split())
#         graph[s].append(e)
#         graph[e].append(s)

#     NEG_INF = float('-inf')
#     SEL, UHSC, UNSC = 0, 1, 2
#     # SEL  : 선정됨
#     # UHSC : 미선정, 자식 중 ≥1개 선정 (조건 3 충족)
#     # UNSC : 미선정, 선정된 자식 없음 (조건 3은 부모가 해결)

#     dp = [[0, NEG_INF, 0] for _ in range(n+1)]

#     # 이터레이티브 DFS로 전위 순서(order) 수집 → reverse = 후위 순서
#     parent = [-1] * (n+1)
#     order = []
#     visited = [False] * (n+1)
#     stack = [(1, 0)]

#     while stack:
#         node, par = stack.pop()
#         if visited[node]:
#             continue
#         visited[node] = True
#         parent[node] = par
#         order.append(node)
#         for nb in graph[node]:
#             if nb != par:
#                 stack.append((nb, node))

#     for v in reversed(order):
#         children = [c for c in graph[v] if c != parent[v]]

#         if not children:          # 리프
#             dp[v] = [people[v], NEG_INF, 0]
#             continue

#         # ── SEL: 자식은 반드시 미선정 (UHSC or UNSC) ──────────────────
#         sel_val = people[v]
#         for c in children:
#             sel_val += max(dp[c][UHSC], dp[c][UNSC])
#         dp[v][SEL] = sel_val

#         # ── UHSC: 자식은 SEL or UHSC, 단 최소 1개는 SEL ──────────────
#         total = 0
#         any_sel = False
#         best_upgrade = NEG_INF          # UHSC→SEL 교체 시 손해 최솟값

#         for c in children:
#             c_sel, c_uhsc = dp[c][SEL], dp[c][UHSC]
#             if c_uhsc == NEG_INF or c_sel >= c_uhsc:
#                 total += c_sel
#                 any_sel = True
#             else:
#                 total += c_uhsc
#                 best_upgrade = max(best_upgrade, c_sel - c_uhsc)

#         if any_sel:
#             dp[v][UHSC] = total
#         elif best_upgrade != NEG_INF:   # 가장 손해 적은 자식 하나 강제 SEL
#             dp[v][UHSC] = total + best_upgrade
#         else:
#             dp[v][UHSC] = NEG_INF

#         # ── UNSC: 자식은 모두 UHSC여야 함 (자식들이 스스로 조건 3 해결) ──
#         unsc_val = 0
#         for c in children:
#             if dp[c][UHSC] == NEG_INF:
#                 unsc_val = NEG_INF
#                 break
#             unsc_val += dp[c][UHSC]
#         dp[v][UNSC] = unsc_val

#     # 루트는 부모가 없으므로 UNSC 상태는 불가
#     print(max(dp[1][SEL], dp[1][UHSC]))

# solve()

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def village(start):
    visited[start] = True

    for i in tree[start]:
        if not visited[i]:
            village(i)
            dp[start][0] += max(dp[i][0], dp[i][1])
            dp[start][1] += dp[i][0]
    
n = int(input())
people = [0] + list(map(int, input().split()))
tree = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
dp = [[0, people[i]] for i in range(n+1)] 
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
village(1)
print(max(dp[1][0], dp[1][1]))