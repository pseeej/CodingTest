T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    times = []

    for _ in range(N):
        times.append(int(input()))

    left, right = 1, max(times)*M
    result = 0
    while left <= right:
        mid = (left+right)//2
        people = 0

        for t in times:
            people += mid//t
            if people >= M:
                result = mid
                right = mid - 1
                break

        if people < M:
            left = mid + 1

    print(f"#{test_case} {result}")
