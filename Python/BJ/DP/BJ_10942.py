import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
m = int(input())

#dp[i][j]: 시작점(i)부터 끝(j)까지의 펠린드롬 여부
dp = [[-1] * n for _ in range(n)]

for i in range(n-1, -1, -1) :
  for j in range(i, n) :
    #길이가 1인 경우
    if i == j :
      dp[i][j] = 1
      continue

    #길이가 2인 경우
    if j-i == 1 and seq[i] == seq[j] :
      dp[i][j] = 1
      continue
    
    #길이가 3이상인 경우
    if dp[i+1][j-1] == 1 and seq[i] == seq[j] :
      dp[i][j] = 1
    else :
      dp[i][j] = 0

answer = []
for _ in range(m) :
  s, e = map(int, input().split())
  answer.append(str(dp[s-1][e-1]))

print("\n".join(answer))