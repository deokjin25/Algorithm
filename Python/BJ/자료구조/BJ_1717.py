import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [-1] * (n + 1)

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    
    if rootA == rootB:
        return
    
    # rank 기반 union
    if parent[rootA] > parent[rootB]:
        parent[rootA] = rootB
    else:
        if parent[rootA] == parent[rootB]:
            parent[rootA] -= 1
        parent[rootB] = rootA

ans = []
for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            ans.append('YES')
        else:
            ans.append('NO')

print('\n'.join(ans))