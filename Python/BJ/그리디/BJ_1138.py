n = int(input())
lst = list(map(int, input().split()))

answer = [-1] * n

for i in range(1,n+1) :
  bigger_cnt = 0
  for j in range(n) :
    if bigger_cnt == lst[i-1] and answer[j] == -1:
      answer[j] = i
      break
    if answer[j] == -1 :
      bigger_cnt+=1

print(*answer)

# def perm(depth, seq, visited) :
#   global answer
#   if len(answer) != 0 :
#     return

#   if depth == n :
#     cnt = [0] * (n+1)
#     for i in range(1,n) :
#       for j in range(i) :
#         if seq[j] > seq[i] :
#           cnt[seq[i]] += 1

#     if cnt[1:] == lst :
#       answer = seq[:]
#     return
  
#   for i in range(1,n+1) :
#     if visited[i] : continue
#     visited[i] = 1
#     seq.append(i)
#     perm(depth+1, seq, visited)
#     seq.pop()
#     visited[i] = 0

# perm(0, [], [0]*(n+1))
# print(*answer)