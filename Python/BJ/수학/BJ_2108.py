import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
mid = (n-1) // 2
lst = [int(input()) for i in range(n)]
lst.sort()

sorted_num_cnt = sorted(Counter(lst).items(), key=lambda x:(-x[1], x[0]))
if len(sorted_num_cnt) == 1 :
  mode_num = sorted_num_cnt[0][0]
else :
  if sorted_num_cnt[0][1] == sorted_num_cnt[1][1] :
    mode_num = sorted_num_cnt[1][0]
  else :
    mode_num = sorted_num_cnt[0][0]

avg = sum(lst)/n
print(int(avg+0.5) if avg > 0 else int(avg-0.5))
print(lst[mid])
print(mode_num)
print(max(lst) - min(lst))