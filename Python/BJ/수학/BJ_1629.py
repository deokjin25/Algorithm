a, b, c = map(int, input().split())

dp = {}

def split_mul(x) :
  if x in dp:
    return dp[x]
  
  if x == 1 :
    return a%c
  
  dp[x] = split_mul(x//2) * split_mul(x - x//2) % c

  return dp[x]

print(split_mul(b)%c)