MOD = 1000000007

def matrix_mult(A, B):
    """2x2 행렬 곱셈"""
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def matrix_pow(M, n):
    """분할 정복을 이용한 행렬 지수화"""
    if n == 1:
        return M
    
    if n % 2 == 0:
        half = matrix_pow(M, n // 2)
        return matrix_mult(half, half)
    else:
        return matrix_mult(M, matrix_pow(M, n - 1))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    M = [[1, 1], [1, 0]]
    result = matrix_pow(M, n)
    return result[0][1]  # F(n)

n = int(input())
print(fibonacci(n))