def dfs(depth, numbers, total, target, answer) :
    if depth == len(numbers) :
        if total == target :
            return answer+1
        else :
            return answer
    
    answer = dfs(depth+1, numbers, total+numbers[depth], target, answer)
    answer = dfs(depth+1, numbers, total-numbers[depth], target, answer)
    
    return answer
    

def solution(numbers, target):
    answer = dfs(0, numbers, 0, target, 0)
    return answer