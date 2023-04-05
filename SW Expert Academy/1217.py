def recur(under, unit, upper, count):
    if count >= upper:
        return under

    return recur(under*unit, unit, upper, count+1)


for _ in range(10):
    test_case = int(input())
    N, M = map(int, input().split())

    print(f"#{test_case} {recur(N, N, M, 1)}")

