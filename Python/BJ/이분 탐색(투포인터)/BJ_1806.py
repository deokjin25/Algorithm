import sys
input = sys.stdin.readline

n, s = map(int, input().split())
seq = list(map(int, input().split()))

left=0

answer = float('inf')
cur = 0
for right in range(n) :
  cur += seq[right]

  while cur >= s :
    answer = min(answer, right-left+1)
    cur -= seq[left]
    left+=1

if answer == float('inf') :
  print(0)
else :
  print(answer)