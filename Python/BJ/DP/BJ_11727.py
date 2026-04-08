n = int(input())
dp = [0] * (n+1)

dp[1] = 1
if n > 1 :
  dp[2] = 3

def n_cases(x) :
  if dp[x] != 0 :
    return dp[x]
  
  dp[x] = n_cases(x-1) + 2 * n_cases(x-2)
  
  return dp[x]%10007

print(n_cases(n))