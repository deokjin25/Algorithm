n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def perm(depth, visited, seq) :
  if depth==m :
    print(*seq)
    return
  
  for idx, val in enumerate(data) :
    if visited[idx] : continue
    visited[idx] = True
    seq.append(val)
    perm(depth+1, visited, seq)
    seq.pop()
    visited[idx]=False

perm(0, [False]*n, [])


# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()

# def perm(depth, visited, sequence) :
#   if depth==m :
#     print(*sequence)
#     return
  
#   for i in data :
#     if visited[i] : continue
#     visited[i] = True
#     sequence.append(i)
#     perm(depth+1, visited, sequence)
#     sequence.pop()
#     visited[i]=False

# perm(0, [False]*10001, [])