s1 = input()
s2 = input()

dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]

for i in range(1,len(s1)+1) :
  for j in range(1,len(s2)+1) :
    if s1[i-1] == s2[j-1] :
      dp[j][i] = dp[j-1][i-1] + 1
    else :
      dp[j][i] = max(dp[j-1][i], dp[j][i-1])

x,y = len(s1), len(s2)
lcs = ''
while x > 0 and y > 0 :
  if s1[x-1] != s2[y-1] :
    if dp[y-1][x] < dp[y][x-1] :
      x -= 1
    else :
      y -= 1
  else :
    lcs = s1[x-1] + lcs
    x-=1
    y-=1

print(dp[-1][-1])
print(lcs)