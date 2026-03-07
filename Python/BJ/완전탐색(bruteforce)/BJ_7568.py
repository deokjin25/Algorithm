n = int(input())

people = [ list(map(int, input().split())) for i in range(n) ]
answer = [0] * n

for i in range(n) :
  x1, y1 = people[i]
  rank = 1
  for j in range(n) :
    if i == j : continue

    x2, y2 = people[j]
    if x1 < x2 and y1 < y2 :
      rank+=1

  answer[i] = rank

print(*answer)