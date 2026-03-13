import sys
input = sys.stdin.readline

def parse_idx(x) :
  return ord(x) - 64

n = int(input())

left = [0] * (n + 1)
right = [0] * (n + 1)
for _ in range(n) :
  p, l, r = input().split()
  p_idx = parse_idx(p)
  left[p_idx]  = 0 if l == '.' else parse_idx(l)
  right[p_idx] = 0 if r == '.' else parse_idx(r)

def preorder(x):
    if x == 0:
        return
    print(chr(x+64), end='')
    preorder(left[x])
    preorder(right[x])

def inorder(x) :
   if x == 0 :
      return
   inorder(left[x])
   print(chr(x+64), end='')
   inorder(right[x])

def postorder(x) :
   if x == 0 :
      return
   postorder(left[x])
   postorder(right[x])
   print(chr(x+64), end='')

preorder(1)
print()
inorder(1)
print()
postorder(1)   