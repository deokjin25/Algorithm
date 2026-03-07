import sys
input = sys.stdin.readline

n = int(input())
answer = []
for _ in range(n) :
  x = int(input())
  if x == 0 and len(answer) != 0:
    answer.pop()
  else :
    answer.append(x)

print(sum(answer))