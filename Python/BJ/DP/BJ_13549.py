from collections import deque

n, k = map(int, input().split())

MAX = 100001
dist = [-1] * MAX
dq = deque()
dq.append(n)
dist[n] = 0

while dq:
    x = dq.popleft()
    if x == k:
        print(dist[k])
        break
    
    # 순간이동 (0초) → deque 앞에 추가
    if x * 2 < MAX and dist[x * 2] == -1:
        dist[x * 2] = dist[x]
        dq.appendleft(x * 2)
    
    # 걷기 (1초) → deque 뒤에 추가
    for nx in [x - 1, x + 1]:
        if 0 <= nx < MAX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            dq.append(nx)