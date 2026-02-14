c, n = map(int, input().split())

dp = [float('inf')] * (c + 101)
dp[0] = 0

cities = []
for _ in range(n) :
  cost, guest = map(int, input().split())
  cities.append((cost, guest))

for i in range(c+101) :
  if dp[i] == float('inf') :
    continue

  for cost, guest in cities :
    if i+guest < c+101 :
      dp[i+guest] = min(dp[i+guest], dp[i]+cost)

print(min(dp[c:c+101]))