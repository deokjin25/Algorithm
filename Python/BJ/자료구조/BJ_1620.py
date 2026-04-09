import sys
input = sys.stdin.readline

n,m = map(int, input().split())

pokemon_name = dict()
pokemon_num = dict()

cnt = 1
for _ in range(n) :
  name = input().strip()
  pokemon_name[name] = cnt
  pokemon_num[cnt] = name
  cnt+=1

answer = []
for _ in range(m) :
  x = input().strip()
  if x.isalpha() :
    answer.append(str(pokemon_name[x]))
  else :
    answer.append(pokemon_num[int(x)])

print('\n'.join(answer))