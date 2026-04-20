import sys
input = sys.stdin.readline

MOD = 1_000_000_000

def solve():
    N = int(input())
    
    # dp[last_digit][visited_bitmask]
    # 초기: 1자리 수 (1~9로 시작, 0으로 시작 불가)
    dp = [[0] * (1 << 10) for _ in range(10)]
    
    for d in range(1, 10):
        dp[d][1 << d] = 1  # 첫 자리 숫자 d, d만 방문
    
    for step in range(N - 1):
        new_dp = [[0] * (1 << 10) for _ in range(10)]
        for last in range(10):
            for visited in range(1 << 10):
                if dp[last][visited] == 0:
                    continue
                cnt = dp[last][visited]
                # 다음 숫자: last-1 또는 last+1
                for nxt in (last - 1, last + 1):
                    if 0 <= nxt <= 9:
                        new_visited = visited | (1 << nxt)
                        new_dp[nxt][new_visited] = (new_dp[nxt][new_visited] + cnt) % MOD
        dp = new_dp
    
    # 0~9 모두 방문한 경우 (bitmask = 1111111111 = 1023)
    ans = 0
    for last in range(10):
        ans = (ans + dp[last][(1 << 10) - 1]) % MOD
    
    print(ans)

solve()