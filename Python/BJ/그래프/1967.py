import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1) :
  s, e, v = map(int, input().split())
  graph[s].append((e,v))

def dfs(x) :
  if not graph[x] :
    return

  for next, v in graph[x] :
    dfs(next)
    max_child = dp[next][0] if dp[next] else 0
    dp[x].append(v + max_child)

  dp[x].sort(reverse=True)

#dp[v][leaf] : v를 중점으로 하는 자식 노드의 최대 길이
dp = [[] for _ in range(n+1)]
dfs(1)
# print(dp)
answer = 0
for x in dp :
  first  = x[0] if len(x) > 0 else 0
  second = x[1] if len(x) > 1 else 0
  answer = max(answer, first + second)
print(answer)