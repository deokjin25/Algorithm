def factorial(n) :
  if n == 1 or n == 0 :
    return 1
  return n * factorial(n-1)

n = int(input())
x = factorial(n)

count = 0
idx = 1
while True :
  if x % (10**idx) != 0 :
    break
  count+=1
  idx+=1

print(count)