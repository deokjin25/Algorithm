n = int(input())
seq = list(map(int,input().split()))

if n == 1 :
  print(seq[0])
else :
  dp = [[0,0] for _ in range(n)]  #[0]: 선택한 경우, [1]: 선택하지 않는 경우
  dp[0] = [seq[0], seq[0]]
  m = seq[0]
  for i in range(1, n) :
    dp[i][0] = max(dp[i-1][0] + seq[i], dp[i-1][1] + seq[i])
    dp[i][1] = seq[i]
    m = max(dp[i][0], dp[i][1], m)
  print(m)
