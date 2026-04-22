def solution(a):
    n = len(a)
    if n <= 2:
        return n

    left_min = [0] * n
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])

    right_min = [0] * n
    right_min[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i])

    answer = 2
    for i in range(1, n-1):
        if a[i] > left_min[i-1] and a[i] > right_min[i+1]:
            continue
        answer += 1

    return answer