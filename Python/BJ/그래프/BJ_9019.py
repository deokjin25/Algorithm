# import sys
# input = sys.stdin.readline
# from collections import deque

# T = int(input())

# def bfs(a, b) :
#   q = deque()
#   q.append((a,[]))
#   dp = [0] * 10000

#   while q :
#     a, cur =  q.popleft()
#     int_a = int(a)

#     if dp[int_a] :
#       continue
#     else :
#       dp[int_a] = 1

#     if int_a == b :
#       print(''.join(cur))
#       return
    
#     # D
#     q.append((str(2*int_a%10000).zfill(4), cur+['D']))

#     # S
#     if int_a == 0 :
#       q.append(('9999', cur+['S']))
#     else :
#       q.append((str(int_a-1).zfill(4), cur+['S']))

#     # L
#     q.append((a[1:] + a[0], cur+['L']))

#     # R
#     q.append((a[-1] + a[0:-1], cur+['R']))

# for _ in range(T) :
#   a, b = input().split()
#   bfs(a.zfill(4), int(b))

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def bfs(start, target):
    visited = [False] * 10000
    prev = [-1] * 10000
    op = [''] * 10000

    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        if cur == target:
            break

        # D
        nxt = (cur * 2) % 10000
        if not visited[nxt]:
            visited[nxt] = True
            prev[nxt] = cur
            op[nxt] = 'D'
            q.append(nxt)

        # S
        nxt = 9999 if cur == 0 else cur - 1
        if not visited[nxt]:
            visited[nxt] = True
            prev[nxt] = cur
            op[nxt] = 'S'
            q.append(nxt)

        # L
        nxt = (cur % 1000) * 10 + (cur // 1000)
        if not visited[nxt]:
            visited[nxt] = True
            prev[nxt] = cur
            op[nxt] = 'L'
            q.append(nxt)

        # R
        nxt = (cur // 10) + (cur % 10) * 1000
        if not visited[nxt]:
            visited[nxt] = True
            prev[nxt] = cur
            op[nxt] = 'R'
            q.append(nxt)

    result = []
    cur = target
    while cur != start:
        result.append(op[cur])
        cur = prev[cur]
    print(''.join(reversed(result)))

for _ in range(T):
    a, b = map(int, input().split())
    bfs(a, b)