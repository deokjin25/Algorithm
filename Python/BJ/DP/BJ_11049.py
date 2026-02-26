import sys
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    r, c = map(int, input().split())
    matrix.append((r, c))

# dp 테이블 초기화 (2차원 배열)
dp = [[0] * n for _ in range(n)]

# 길이(length)를 기준으로 DP 수행
for length in range(1, n):  # 곱할 행렬의 개수 - 1
    for i in range(n - length):
        j = i + length
        dp[i][j] = float('inf')
        
        # i~j를 k를 기준으로 분할
        for k in range(i, j):
            # (i~k) 곱셈 + (k+1~j) 곱셈 + 두 결과 행렬의 곱셈
            cost = dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])