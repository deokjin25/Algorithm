import sys
input = sys.stdin.readline

import bisect

n = int(input())
liquids = list(map(int, input().split()))

acids=[]
alkalines=[]
for liquid in liquids :
  if liquid <= 0 :
    alkalines.append(liquid)
  else :
    acids.append(liquid)

x, y = float('inf'), float('inf')
best = float('inf')

if len(alkalines) >= 2 :
  x, y = alkalines[-2], alkalines[-1]
  best = abs(x+y)

if len(acids) >= 2 and best > abs(acids[1] - acids[0]) :
  x, y = acids[0], acids[1]
  best = abs(x+y)


for alkaline in alkalines :
  idx = bisect.bisect_left(acids, -alkaline)
  
  for i in [idx-1, idx] :
    if 0 <= i < len(acids) :
      current = abs(alkaline + acids[i])
      if best > current :
        best = current
        x,y = alkaline, acids[i]

print(x, y)