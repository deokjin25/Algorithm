import sys
input = sys.stdin.readline

n = int(input())
seq = sorted(map(int, input().split()))

count = 0
for k in range(n):
    target = seq[k]
    left, right = 0, n - 1

    while left < right:
        s = seq[left] + seq[right]
        if s == target:
            if left != k and right != k:  # 자기 자신 인덱스 제외
                count += 1
                break
            elif left == k:
                left += 1
            else:
                right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1

print(count)