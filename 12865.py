import sys
input = sys.stdin.readline

N, K = map(int, input().split())
DP = [[0 for _ in range(N+1)] for _ in range(K+1)]

weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

for i in range(1, K+1):
    for j in range(N):
        if weights[j] > i:
            DP[i][j] = DP[i][j-1]
        
        else:
            DP[i][j] = max(DP[i][j-1], DP[i-weights[j]][j-1]+values[j])


print(DP[K][N-1])
        
