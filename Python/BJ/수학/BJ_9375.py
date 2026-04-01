# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T) :
#   n = int(input())

#   if n == 0 :
#     print(0)
#     continue

#   clothes = {}
#   for _ in range(n) :
#     name, category = input().split()
#     if clothes.get(category, 0) == 0 :
#       clothes[category] = [name]
#     else :
#       clothes[category].append(name)

#   answer = 1
#   for category in clothes :
#     answer *= (len(clothes[category]) + 1)
#   print(answer - 1)

import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    
    if n == 0:
        print(0)
        continue
    
    clothes = defaultdict(int)
    for _ in range(n):
        name, category = input().split()
        clothes[category] += 1  # 개수만 세기
    
    answer = 1
    for count in clothes.values():  # 카테고리별 개수로 계산
        answer *= (count + 1)
    print(answer - 1)