N = int(input())
building = list(map(int, input().split()))
answer = 0

for i in range(N):
    count = 0
    
    # 오른쪽 탐색
    max_slope = float('-inf')
    for j in range(i + 1, N):
        slope = (building[j] - building[i]) / (j - i)
        if slope > max_slope:
            count += 1
            max_slope = slope  # 기울기 갱신
    
    # 왼쪽 탐색
    max_slope = float('-inf')
    for j in range(i - 1, -1, -1):
        slope = (building[j] - building[i]) / (i - j)
        if slope > max_slope:
            count += 1
            max_slope = slope
    
    answer = max(count, answer)

print(answer)