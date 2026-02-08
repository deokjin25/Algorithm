s = input()

stack = []

answer = 0
for i in range(len(s)) :
  if s[i] == ')' :
    stack.pop()
    if s[i-1] == '(' :
      answer += len(stack)
    else :
      answer += 1
  else :
    stack.append(s[i])

print(answer)