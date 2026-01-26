x = int(input())
count = 0
num = 0

while True :
  num+=1
  if str(num).count('666') >= 1 :
    count+=1
  
  if count == x :
    print(num)
    break