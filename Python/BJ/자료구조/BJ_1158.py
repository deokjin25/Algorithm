# from collections import deque

# n, k = map(int, input().split())

# q = deque(range(1,n+1))

# cnt = 0
# answer = []
# while q :
#   cnt += 1
#   x = q.popleft()
#   if cnt % k != 0 :
#     q.append(x)
#   else :
#     answer.append(str(x))

# print(f'<{(', ').join(answer)}>')

n, k = map(int, input().split())

q = list(range(1,n+1))

idx = 0
answer = []
while q :
  idx = (idx+k-1) % len(q)
  answer.append(str(q.pop(idx)))

print(f'<{(', ').join(answer)}>')