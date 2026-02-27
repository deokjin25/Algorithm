import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

best = 10e9
x,y,z = liquids[0], liquids[1], liquids[2]

for i in range(n-2) :
  left = i+1
  right = n-1

  while left < right :
    total = liquids[i] + liquids[left] + liquids[right]

    if abs(total) < best :
      best = abs(total)
      x,y,z = liquids[i], liquids[left], liquids[right]

    if total < 0 :
      left +=1
    elif total > 0 :
      right -= 1
    else :
      break

print(x,y,z)

# acids = []
# alkalines = []

# for liquid in liquids :
#   if liquid < 0 :
#     alkalines.append(liquid)
#   else :
#     acids.append(liquid)

# liquids.sort()
# alkalines.sort()
# acids.sort()

# x, y, z = 10e9, 10e9, 10e9
# best = 10e9
# #알칼리 3
# if len(alkalines) > 2 :
#   x, y, z = alkalines[-3], alkalines[-2], alkalines[-1]
#   best = abs(x+y+z)

# #산성 3
# if len(acids) > 2 and best > (acids[0] + acids[1] + acids[2]):
#   x, y, z = acids[0], acids[1], acids[2]
#   best = x+y+z

# # 알칼리 1
# for i in range(len(alkalines)) :
#   # 알칼리 2
#   for j in range(i+1, len(alkalines)) :
#     mix_liquid = alkalines[i] + alkalines[j]
#     # 산성 1
#     idx = bisect_left(acids, -mix_liquid)
#     for k in [idx-1, idx] :
#       if 0<=k<len(acids) and best > abs(acids[k]+mix_liquid) :
#         best = abs(acids[k]+mix_liquid)
#         x,y,z = alkalines[i], alkalines[j], acids[k]

# # 산성 1
# for i in range(len(acids)) :
#   # 산성 2
#   for j in range(i+1, len(acids)) :
#     mix_liquid = acids[i] + acids[j]
#     # 알칼리 1
#     idx = bisect_left(alkalines, -mix_liquid)
#     for k in [idx-1, idx] :
#       if 0<=k<len(alkalines) and best > abs(alkalines[k] + mix_liquid) :
#         best = abs(alkalines[k] + mix_liquid)
#         x,y,z = alkalines[k], acids[i], acids[j]

# print(x,y,z)

# #각 용액 2가지 섞기
# mix_alkalines = []
# for i in range(len(alkalines)) :
#   for j in range(i+1, len(alkalines)) :
#     mix_alkalines.append((alkalines[i], alkalines[j]))

# mix_acids = []
# for i in range(len(acids)) :
#   for j in range(i+1, len(acids)) :
#     mix_acids.append((acids[i], acids[j]))

# #섞인 2가지 용액과 원액 섞기(3가지)
# for mix_alkaline in mix_alkalines :
#   liquid_a, liquid_b = mix_alkaline
#   mix_liquid = liquid_a + liquid_b
#   idx = bisect_left(acids, -mix_liquid)

#   for i in [idx-1, idx] :
#     if 0<= i < len(acids) and best > abs(acids[i] + mix_liquid):
#       best = abs(acids[i] + mix_liquid)
#       x,y,z = liquid_a, liquid_b, acids[i]

# for mix_acid in mix_acids :
#   liquid_a, liquid_b = mix_acid
#   mix_liquid = liquid_a + liquid_b
#   idx = bisect_left(alkalines, -mix_liquid)

#   for i in [idx-1, idx] :
#     if 0 <= i < len(alkalines) and best > abs(alkalines[i] + mix_liquid) :
#       best = abs(alkalines[i] + mix_liquid)
#       x,y,z = alkalines[i], liquid_a, liquid_b

# print(x,y,z)