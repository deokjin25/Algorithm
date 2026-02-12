import sys
input = sys.stdin.readline

def get_cost(from_pos, to_pos):
    """발을 from_pos에서 to_pos로 이동할 때 드는 힘"""
    if from_pos == to_pos:
        return 1
    if from_pos == 0:  # 중앙에서 시작
        return 2
    if abs(from_pos - to_pos) == 2:  # 반대편
        return 4
    return 3  # 인접

directions = list(map(int, input().split()))
directions.pop()  # 마지막 0 제거

# dp[왼발위치][오른발위치] = 최소 힘
dp = [[float('inf')] * 5 for _ in range(5)]
dp[0][0] = 0

for move in directions:
    new_dp = [[float('inf')] * 5 for _ in range(5)]
    
    for left in range(5):
        for right in range(5):
            if dp[left][right] == float('inf'):
                continue
            
            # 왼발을 move로 이동
            if move != right:
                new_dp[move][right] = min(new_dp[move][right], 
                                          dp[left][right] + get_cost(left, move))
            
            # 오른발을 move로 이동
            if move != left:
                new_dp[left][move] = min(new_dp[left][move], 
                                          dp[left][right] + get_cost(right, move))
    
    dp = new_dp

# 최소값 찾기
answer = float('inf')
for left in range(5):
    for right in range(5):
        answer = min(answer, dp[left][right])

print(answer)