s1 = input()
s2 = input()

dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]

for i in range(1,len(s1)+1) :
  for j in range(1,len(s2)+1) :
    if s1[i-1] == s2[j-1] :
      dp[j][i] = dp[j-1][i-1] + 1
    else :
      dp[j][i] = max(dp[j-1][i], dp[j][i-1])

print(dp[-1][-1])



# import sys
# input = sys.stdin.readline

# def LCS(strA, strB) :
# 	dp = [0] * 1000

# 	for a in strA:
# 		cnt = 0
# 		for j, b in enumerate(strB):
# 			if cnt < dp[j]:
# 				cnt = dp[j]
# 			elif a == b:
# 				dp[j] = cnt + 1
	
# 	return max(dp)

# strA = input().rstrip()
# strB = input().rstrip()
# print(LCS(strA, strB))