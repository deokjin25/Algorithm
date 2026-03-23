# import sys
# input = sys.stdin.readline

# n = int(input())
# scores = [ list(map(int, input().split())) for _ in range(n) ]

# max_dp = [ [0,0,0] for _ in range(n+1) ]
# min_dp = [ [0,0,0] for _ in range(n+1) ]

# for i in range(1,n+1) :
#   #왼쪽
#   max_dp[i][0] = max(scores[i-1][0] + max_dp[i-1][0], scores[i-1][0] + max_dp[i-1][1])
#   min_dp[i][0] = min(scores[i-1][0] + min_dp[i-1][0], scores[i-1][0] + min_dp[i-1][1])

#   #중간
#   max_dp[i][1] = max(scores[i-1][1] + max_dp[i-1][0], scores[i-1][1] + max_dp[i-1][1], 
#                      scores[i-1][1] + max_dp[i-1][2])
#   min_dp[i][1] = min(scores[i-1][1] + min_dp[i-1][0], scores[i-1][1] + min_dp[i-1][1],
#                      scores[i-1][1] + min_dp[i-1][2])
  
#   #오른쪽
#   max_dp[i][2] = max(scores[i-1][2] + max_dp[i-1][1], scores[i-1][2] + max_dp[i-1][2])
#   min_dp[i][2] = min(scores[i-1][2] + min_dp[i-1][1], scores[i-1][2] + min_dp[i-1][2])

# print(max(max_dp[-1]), min(min_dp[-1]))

# import sys
# input = sys.stdin.readline

# n = int(input())

# dp = [ [[0,0,0] for _ in range(2)] for _ in range(n+1) ]

# for i in range(1,n+1) :
#   a, b, c = map(int, input().split())

#   #왼쪽
#   dp[i][0][0] = max(a + dp[i-1][0][0], a + dp[i-1][0][1])
#   dp[i][1][0] = min(a + dp[i-1][1][0], a + dp[i-1][1][1])

#   #중간
#   dp[i][0][1] = max(b + dp[i-1][0][0], b + dp[i-1][0][1], 
#                      b + dp[i-1][0][2])
#   dp[i][1][1] = min(b + dp[i-1][1][0], b + dp[i-1][1][1],
#                      b + dp[i-1][1][2])
  
#   #오른쪽
#   dp[i][0][2] = max(c + dp[i-1][0][1], c + dp[i-1][0][2])
#   dp[i][1][2] = min(c + dp[i-1][1][1], c + dp[i-1][1][2])

# print(max(dp[-1][0]), min(dp[-1][1]))

import sys
input = sys.stdin.readline

n = int(input())

tmp_max_a, tmp_max_b, tmp_max_c = 0,0,0
tmp_min_a, tmp_min_b, tmp_min_c = 0,0,0
max_a, max_b, max_c = 0,0,0
min_a, min_b, min_c = 0,0,0

for i in range(1,n+1) :
  a, b, c = map(int, input().split())

  #왼쪽
  max_a = max(a + tmp_max_a, a + tmp_max_b)
  min_a = min(a + tmp_min_a, a + tmp_min_b)

  #중간
  max_b = max(b + tmp_max_a, b + tmp_max_b, b + tmp_max_c)
  min_b = min(b + tmp_min_a, b + tmp_min_b, b + tmp_min_c)
  
  #오른쪽
  max_c = max(c + tmp_max_b, c + tmp_max_c)
  min_c = min(c + tmp_min_b, c + tmp_min_c)

  tmp_max_a, tmp_max_b, tmp_max_c = max_a, max_b, max_c
  tmp_min_a, tmp_min_b, tmp_min_c = min_a, min_b, min_c

print(max(max_a, max_b, max_c), min(min_a, min_b, min_c))