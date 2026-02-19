import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = []

for num in arr:
    # dp에서 num이 들어갈 위치를 이분 탐색
    pos = bisect_left(dp, num)
    
    if pos == len(dp):
        # num이 가장 크면 뒤에 추가
        dp.append(num)
    else:
        # 해당 위치의 값을 num으로 교체
        dp[pos] = num

print(len(dp))