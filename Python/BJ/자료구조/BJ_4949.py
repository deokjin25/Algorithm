import sys
input = sys.stdin.readline

answer = []

while True :
  s = input().rstrip()
  if s == '.' : break

  stack = []

  flag = True
  for i in range(len(s)) :
    if s[i] == '(' :
      stack.append('(')
    elif s[i] == ')' :
      if len(stack) != 0 and stack[-1] == '(' :
        stack.pop()
      else :
        flag = False
        break
    elif s[i] == '[' :
      stack.append('[')
    elif s[i] == ']' :
      if len(stack) != 0 and stack[-1] == '[' :
        stack.pop()
      else :
        flag = False
        break
  
  if flag and len(stack) == 0 :
    answer.append('yes')
  else :
    answer.append('no')

print(('\n').join(answer))