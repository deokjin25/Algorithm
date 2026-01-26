n, m = map(int, input().split())

def combR(depth, idx, sequence) :
  if depth == m : 
    print(*sequence)
    return
  
  for i in range(idx, n+1) :
    sequence.append(i)
    combR(depth+1, i, sequence)
    sequence.pop()

combR(0, 1, [])