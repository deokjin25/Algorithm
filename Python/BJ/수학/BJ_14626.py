ISBN=input()

w = 1
s = 0 
for idx, val in enumerate(ISBN) :
  if val == '*' : 
    if idx%2 == 1 : 
      w = 3
    continue
  num = int(val)
  num = num if idx%2==0 else 3*num
  s += num

x = 10 - s%10

if x == 10 :
  print(0)
elif x%w == 0 :
  print(int((10 - s%10)/w))
else :
  for i in range(1,10) :
    if (i*w + s)%10 == 0 :
      print(i)
      break