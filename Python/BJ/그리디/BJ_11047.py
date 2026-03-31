import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coin = [ int(input()) for _ in range(n) ]

answer = 0
for i in range(n-1, -1, -1) :
  x = k//coin[i]
  if x > 0 :
    answer += x
    k%=coin[i]

print(answer)