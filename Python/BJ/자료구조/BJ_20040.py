import sys
input = sys.stdin.readline

n, m  = map(int, input().split())

parent = list(range(n))

def find(x) :
  if x != parent[x] :
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b) :
  rootA = find(a)
  rootB = find(b)

  if rootA == rootB :
    return True
  
  if rootA < rootB :
    parent[rootB] = rootA
  else :
    parent[rootA] = rootB

  return False

def solution() :
  for i in range(m) :
    s, e = map(int, input().split())
    if union(s, e) :
      print(i+1)
      return
  
  print(0)
  return

solution()