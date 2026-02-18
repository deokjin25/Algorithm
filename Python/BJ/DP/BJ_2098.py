import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
cost_graph = []
for _ in range(n) :
  cost_graph.append(list(map(int, input().split())))

dp = [[-1] * (1<<n) for _ in range(n)]

def tsp(current, visited) :
  if visited == (1 << n) - 1 :
    back = cost_graph[current][0]
    if back != 0 :
      return back
    else :
      return float('inf')
    
  # 이미 계산한 적 있으면 바로 리턴
  if dp[current][visited] != -1:
      return dp[current][visited]
  
  dp[current][visited] = float('inf')
  
  for i in range(n) :
    # 방문한 도시라면
    if visited & (1<<i) :
      continue

    # 이동할 수 없으면
    if cost_graph[current][i] == 0 :
      continue

    next_cost = cost_graph[current][i] + tsp(i, visited | (1<<i))
    dp[current][visited] = min(dp[current][visited], next_cost)

  return dp[current][visited]

print(tsp(0, 1<<0))