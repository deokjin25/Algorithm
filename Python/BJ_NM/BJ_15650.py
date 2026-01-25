n, m = map(int, input().split())

def comb(depth, sequence, visited, index) :
  if depth == m :
    print(*sequence)
    return

  for i in range(index, n+1) :
    if visited[i] : continue
    visited[i] = True
    sequence.append(i)
    comb(depth+1, sequence, visited, i)
    sequence.pop()
    visited[i]=False

comb(0, [], [False] * (n+1), 1)