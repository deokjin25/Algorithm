import sys
input = sys.stdin.readline

from bisect import bisect_left

n, m = map(int, input().split())

titles = []
powers = []

for _ in range(n):
    title, power = input().split()
    power = int(power)
    # 중복된 전투력은 첫 번째 칭호만 저장
    if not powers or powers[-1] != power:
        titles.append(title)
        powers.append(power)

# def binary_search(target):
#     left, right = 0, len(powers) - 1
#     result = 0
    
#     while left <= right:
#         mid = (left + right) // 2
        
#         if powers[mid] >= target:
#             result = mid
#             right = mid - 1
#         else:
#             left = mid + 1
    
#     return result

# for _ in range(m):
#     character_power = int(input())
#     idx = binary_search(character_power)
#     print(titles[idx])


for _ in range(m) :
    character_power = int(input())
    idx = bisect_left(powers, character_power)
    print(titles[idx])