import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
array = list(map(int, input().split()))
array = sorted(array, reverse=False)

calcs = [0 for i in range(N+1)]
for i in range(1, N+1):
    calcs[i] = calcs[i-1] + array[i-1]

for _ in range(Q):
    l, r = map(int, input().split())
    print(calcs[r]-calcs[l-1])
