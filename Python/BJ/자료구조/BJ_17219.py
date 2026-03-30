import sys
input = sys.stdin.readline

n,m = map(int, input().split())

f = dict()
for _ in range(n) :
  url, pwd = input().split()
  f[url] = pwd

for _ in range(m) :
  x = input().strip()
  print(f[x])