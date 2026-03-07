import sys
input = sys.stdin.readline

def round_half_up(x):
    return int(x + 0.5)

n = int(input())
if n == 0:
    print(0)
else:
    cut = round_half_up(n * 0.15)
    answer = [int(input()) for _ in range(n)]
    answer.sort()
    remaining = answer[cut:n - cut]
    total = sum(remaining)
    count = len(remaining)
    print((total * 2 + count) // (count * 2))