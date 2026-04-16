from collections import Counter

n = int(input())
word = input()

def is_similar(a, b):
    ca, cb = Counter(a), Counter(b)
    
    diff = 0
    all_keys = set(ca.keys()) | set(cb.keys())
    for k in all_keys:
        diff += abs(ca.get(k, 0) - cb.get(k, 0))
    
    length_diff = abs(len(a) - len(b))
    
    if length_diff == 0 and diff in (0, 2):
        return True
    if length_diff == 1 and diff == 1:
        return True
    return False

answer = 0
for _ in range(n - 1):
    x = input()
    if is_similar(word, x):
        answer += 1

print(answer)