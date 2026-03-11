import sys
from collections import deque
input = sys.stdin.readline

s = list(input().rstrip())
left = deque(s)   # 커서 왼쪽 문자들 (top = 커서 바로 왼쪽)
right = deque()   # 커서 오른쪽 문자들 (front = 커서 바로 오른쪽)

for _ in range(int(input())):
    order = input().rstrip()
    if order == 'L':
        if left:
            right.appendleft(left.pop())
    elif order == 'D':
        if right:
            left.append(right.popleft())
    elif order == 'B':
        if left:
            left.pop()
    else:
        left.append(order[2:])

print(''.join(left) + ''.join(right))