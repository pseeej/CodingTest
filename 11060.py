N = int(input())
jumps = list(map(int, input().split()))

# 여기의 i번째에는.. i번째까지 오는 방법의 최솟값을 적어두자.
dp = [float("inf") for _ in range(N)]

dp[0] = 0
for curidx in range(N-1):
    for jump in range(1, jumps[curidx]+1):
        # print(curidx, jump, curidx+jump)
        if curidx+jump < N:
            dp[curidx+jump] = min(dp[curidx]+1, dp[curidx+jump])

print(dp[-1])
