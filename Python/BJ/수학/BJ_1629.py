a, b, c = map(int, input().split())

# dp = {}

# def split_mul(x) :
#   if x in dp:
#     return dp[x]
  
#   if x == 1 :
#     return a%c
  
#   dp[x] = split_mul(x//2) * split_mul(x - x//2) % c

#   return dp[x]

# print(split_mul(b))

# print(pow(a,b,c))

def split_mul(x):
    if x == 1:
        return a % c
    half = split_mul(x // 2)
    if x % 2 == 0:
        return half * half % c
    else:
        return a % c * half * half % c  # 홀수면 a 한 번 더 곱
    
print(split_mul(b))