import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    num = 0
    checkIfFalse = True

    while True:
        if (M*num + x - y)%N == 0:
            break
        if (M*num + x - y) > M*N:
            checkIfFalse = False
            break

        num += 1

    if checkIfFalse:
        print(M*num+x)
    else:
        print(-1)
