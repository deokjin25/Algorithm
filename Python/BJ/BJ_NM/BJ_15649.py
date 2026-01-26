n, m = map(int, input().split())

def perm(depth, sequence, visited) :
  if depth == m :
    print(*sequence)
    return

  for i in range(1, n+1) :
    if visited[i] : continue
    visited[i] = True
    sequence.append(i)
    perm(depth+1, sequence, visited)
    sequence.pop()
    visited[i]=False

perm(0, [], [False] * (n+1))