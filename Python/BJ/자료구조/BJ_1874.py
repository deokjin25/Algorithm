from collections import deque

n = int(input())
seq = []
for _ in range(n) :
  seq.append(int(input()))

stack = []
stack_num = 1
idx = 0
answer = []
while stack_num <= n and idx < n :
  if len(stack) != 0 and stack[-1] == seq[idx] :
    stack.pop()
    answer.append('-')
    idx+=1
    continue
  stack.append(stack_num)
  stack_num+=1
  answer.append('+')

while len(stack) != 0 and idx < n:
  if stack.pop() == seq[idx] :
    idx += 1
  answer.append('-')

if idx == n :
  for i in answer :
    print(i)
else :
  print('NO')