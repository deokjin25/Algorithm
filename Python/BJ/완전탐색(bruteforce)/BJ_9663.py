n = int(input())

def Queen(r, c, _chess, total) :
  if total == n :
    return 1
  
  tmp_chess = [ _chess[i][:] for i in range(n)]
  
  #하단
  tmp=1
  while r+tmp < n :
    tmp_chess[r+tmp][c] = 0
    tmp+=1

  #왼측 대각선
  tmp=1
  while r+tmp < n and c-tmp >= 0 :
    tmp_chess[r+tmp][c-tmp] = 0
    tmp+=1
  
  #우측 대각선
  tmp=1
  while r+tmp < n and c+tmp < n :
    tmp_chess[r+tmp][c+tmp] = 0
    tmp += 1

  possible = 0
  # for i in range(r+1,n) :
  #   for j in range(n) :
  #     if tmp_chess[i][j] == 1 :
  #       possible += Queen(i,j,tmp_chess,total+1)

  for i in range(n) :
    if tmp_chess[r+1][i] == 1 :
      possible += Queen(r+1,i,tmp_chess,total+1)

  return possible

# answer = 0
# chess = [[1]*n for _ in range(n)]
# for i in range(n) :
#   answer += Queen(0, i, chess, 1)

# print(answer)

answer = 0
def count_Q(depth, cols, diag1, diag2) :
  global answer

  if depth == n :
    answer += 1
    return
  
  for i in range(n) :
    if i not in cols and (depth - i) not in diag1 and (depth + i) not in diag2 :
      cols.add(i)
      diag1.add(depth - i)
      diag2.add(depth + i)
      count_Q(depth + 1, cols, diag1, diag2)
      cols.remove(i)
      diag1.remove(depth - i)
      diag2.remove(depth + i)

count_Q(0, set(), set(), set())
print(answer)
