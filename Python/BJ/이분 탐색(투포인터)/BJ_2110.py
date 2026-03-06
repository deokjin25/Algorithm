import sys
input = sys.stdin.readline

n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()

def can_install(min_dist):
    count = 1
    last = homes[0]
    for home in homes[1:]:
        if home - last >= min_dist:
            count += 1
            last = home
            if count >= c:
                return True
    return count >= c

left, right = 1, homes[-1] - homes[0]
answer = 0
while left <= right:
    mid = (left + right) // 2
    if can_install(mid):
        answer = mid
        left = mid + 1   # 더 큰 최소거리 가능한지 탐색
    else:
        right = mid - 1

print(answer)