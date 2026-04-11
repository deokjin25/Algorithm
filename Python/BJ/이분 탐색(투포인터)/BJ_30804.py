import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
tanghuru = list(map(int, input().split()))
left = 0
max_len = 0
c = Counter()

for right in range(n):
    c[tanghuru[right]] += 1

    while len(c) > 2:
        c[tanghuru[left]] -= 1
        if c[tanghuru[left]] == 0:
            del c[tanghuru[left]]
        left += 1
    
    max_len = max(max_len, right - left + 1)

print(max_len)