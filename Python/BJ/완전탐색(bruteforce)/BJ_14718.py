# 방법1
# import sys
# input = sys.stdin.readline
# import heapq

# class soldier :
#   def __init__(self, str, dex, int_) :
#     self.str = str
#     self.dex = dex
#     self.int_ = int_

#   def power(self) :
#     return self.str + self.dex + self.int_

# n, k = map(int, input().split())
# soldier_list = [list(map(int, input().split())) for _ in range(n)]

# str = []
# dex = []
# int_ = []
# soldier_power = []

# cnt = 0
# for s_str, s_dex, s_int_ in soldier_list :
#   s = soldier(s_str, s_dex, s_int_)

#   if cnt < k :
#     heapq.heappush(str, -s.str)
#     heapq.heappush(dex, -s.dex)
#     heapq.heappush(int_, -s.int_)
#     heapq.heappush(soldier_power, -s.power())
#     cnt+=1
#     continue

#   if -(soldier_power[0]) > s.power() :
#     heapq.heappop(soldier_power)
#     heapq.heappush(soldier_power, -s.power())
  
# print(str+dex+int_)

# 방법 2
# import itertools

# n, k = map(int, input().split())
# soldier_list = [list(map(int, input().split())) for _ in range(n)]

# answer = 10e8
# for c in itertools.combinations(soldier_list, k) :
#   s = 0
#   d = 0
#   i = 0
#   for str, dex, int in c :
#     s = max(s, str)
#     d = max(d, dex)
#     i = max(i, int)

#   answer = min(s+d+i, answer)

# print(answer)

# 방법 3
# n, k = map(int, input().split())
# soldier_list = [list(map(int, input().split())) for _ in range(n)]

# answer_x, answer_y, answer_z = 0, 0, 0

# winable_s = []

# for i in range(k) :
#   x, y, z = soldier_list[i]
#   winable_s.append(soldier_list[i])
#   answer_x = max(answer_x, x)
#   answer_y = max(answer_y, y)
#   answer_z = max(answer_z, z)

# for i in range(k, len(soldier_list)) :
#   diff = 0
#   idx = -1
#   for j in range(k) :
#     if sum(soldier_list[i]) < sum(winable_s[j]) :
#       diff = min(diff, sum(soldier_list[i]) - sum(winable_s[j]))
#       idx = j

#   if diff < 0 :
#     winable_s.pop(idx)
#     winable_s.append(soldier_list[i])
#     answer_x, answer_y, answer_z = 0, 0, 0
#     for x, y, z in winable_s :
#       answer_x = max(answer_x, x)
#       answer_y = max(answer_y, y)
#       answer_z = max(answer_z, z)

# print(answer_x + answer_y + answer_z)

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
soldiers = [tuple(map(int, input().split())) for _ in range(n)]

INF = 10**18
answer = INF

for s_ref in soldiers:          # 힘 기준 후보
    S = s_ref[0]
    for d_ref in soldiers:      # 민첩 기준 후보
        D = d_ref[1]
        ints = [c for a, b, c in soldiers if a <= S and b <= D]
        if len(ints) < k:
            continue
        ints.sort()
        C = ints[k - 1]         # k번째로 작은 지능이 필요
        answer = min(answer, S + D + C)

print(answer)