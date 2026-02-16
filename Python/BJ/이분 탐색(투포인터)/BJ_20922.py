# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())

# answer = 0
# seq = list(map(int, input().split()))

# right, left = 0, 0

# num = dict()

# for right in range(n) :
#   x = seq[right]

#   try :
#     num[x] += 1
#   except :
#     num[x] = 1

#   if num[x] > k :
#     while left < right :
#       y = seq[left]
#       num[y] -= 1
#       left+=1
#       if num[x] <= k :
#         break
  
#   answer = max(answer, right - left + 1)

# print(answer)

import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().split()))

answer = 0
left = 0
count = defaultdict(int)

for right in range(n):
    count[seq[right]] += 1
    
    while count[seq[right]] > k:
        count[seq[left]] -= 1
        left += 1
    
    answer = max(answer, right - left + 1)

print(answer)