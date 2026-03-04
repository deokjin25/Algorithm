import sys
input = sys.stdin.readline

from bisect import bisect_left

n, score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    rank_list = list(map(int, input().split()))
    rank = bisect_left([-x for x in rank_list], -score) + 1
    print(-1 if p < rank + rank_list.count(score) else rank)

# if n == 0 :
#   print(1)
# else :
#   rank_list = list(map(int, input().split()))

#   answer = 1
#   tmp = 0

#   for i in range(len(rank_list)) :
#     if score >= rank_list[i] :
#       break
#     elif i > 0 and (rank_list[i-1] == rank_list[i]) :
#       tmp+=1
#     elif score < rank_list[i] :
#       answer += (1 + tmp)
#       tmp = 0

#   if tmp != 0 :
#     answer += tmp

#   if p < (answer+rank_list.count(score)) :
#     print(-1)
#   else :
#     print(answer)
