n, m = map(int, input().split())

def permR(depth, sequence) :
  if depth == m :
    print(*sequence)
    return

  for i in range(1, n+1) :
    sequence.append(i)
    permR(depth+1, sequence)
    sequence.pop()

permR(0, [])