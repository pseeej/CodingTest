T = int(input())

for test_case in range(1, T+1):
    day, month, tmonths, year = map(int, input().split())
    usage = list(map(int, input().split()))

    dp = [0 for _ in range(12)]
    used3mo = []

    for i in range(12):
        # 하루당 / 한달 비교
        dp[i] = min(usage[i]*day, month) + dp[i-1]
        # 세달 비교
        if i >= 2:
            dp[i] = min(dp[i-3]+tmonths, dp[i])

    # 1년 비교
    result = min(dp[-1], year)
    print(f"#{test_case} {result}")
