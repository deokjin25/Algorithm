import sys
input = sys.stdin.readline

s = input().rstrip()
window_size = s.count('a')

answer = 10e9
for i in range(len(s)) :
  idx = i+window_size
  if idx >= len(s) : 
    answer = min(answer, s[i:len(s)].count('b') + s[:idx-len(s)].count('b'))
  else :
    answer = min(answer, s[i:idx].count('b'))

print(answer)