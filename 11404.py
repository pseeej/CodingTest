N = int(input())
K = int(input())

arr = [[int(1e9) for i in range(N+1)] for i in range(N+1)]

for i in range(K):
    a, b, c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)

for i in range(N+1):
    arr[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])


for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == int(1e9):
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()