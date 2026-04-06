# import sys
# input = sys.stdin.readline

# k,n = map(int, input().split())
# lans = [ int(input()) for _ in range(k) ]

# l = 1
# r = max(lans)
# answer = 0
# while l <= r :
#   mid = (l+r) // 2

#   cnt = 0
#   for lan in lans :
#     cnt += lan//mid
  
#   if cnt < n :
#     r = mid-1 
#   else :
#     l = mid+1
#     answer = max(answer, mid)

# print(answer)

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

l = 1
r = max(lans)
while l <= r:
    mid = (l + r) // 2
    cnt = sum(lan // mid for lan in lans)  # sum()으로 더 간결하게
    if cnt >= n:
        l = mid + 1
    else:
        r = mid - 1

print(r)  # r이 최대 길이