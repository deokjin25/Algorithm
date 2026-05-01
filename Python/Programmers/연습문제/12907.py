# def solution(n, money):
#     answer = 0
    
#     def dfs(idx, remain) :
#         nonlocal answer

#         if remain == 0 :
#             answer += 1
#             return
            
#         if remain < 0 :
#             return
        
#         for i in range(idx, len(money)) :
#             cnt = 1
#             while money[i] * cnt <= remain :
#                 dfs(i+1, remain - money[i] * cnt)
#                 cnt+=1
#     dfs(0, n)
#     return answer
# print(solution(5, [1,2,5]))

def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
    return dp[n] % 1000000007

print(solution(5, [1,2,5]))