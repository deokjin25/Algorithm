# a, b = map(int, input().split())

# answer = 10e9
# def solve(x, t) :
#   global answer

#   if x > b :
#     return
  
#   if x == b :
#     answer = min(answer, t)
#     return
  
#   solve(x*2, t+1)
#   solve(int(str(x)+'1'), t+1)

# solve(a, 1)
# if answer == 10e9 :
#   print(-1)
# else :
#   print(answer)

from collections import deque

a, b = map(int, input().split())

queue = deque([(a, 1)])
found = False

while queue:
    x, t = queue.popleft()
    
    if x == b:
        print(t)
        found = True
        break
    
    if x > b:
        continue
    
    queue.append((x * 2, t + 1))
    queue.append((x * 10 + 1, t + 1))

if not found:
    print(-1)