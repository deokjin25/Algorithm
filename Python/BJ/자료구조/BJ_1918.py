def precedence(op):
    if op in '*/':
        return 2
    elif op in '+-':
        return 1
    return 0

def infix_to_postfix(expression):
    stack = []
    result = []
    for char in expression:
        if char.isalpha():  # 피연산자 (알파벳)
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:
                stack.pop()  # '(' 제거
        else:  # 연산자
            while stack and precedence(stack[-1]) >= precedence(char):
                result.append(stack.pop())
            stack.append(char)
    
    while stack:
        result.append(stack.pop())
    
    return ''.join(result)

# 입력 처리
data = input().strip()
print(infix_to_postfix(data))
