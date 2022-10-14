import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N
for i in range(N):
    A[i] -= B
    if A[i] <= 0:
        continue

    if A[i] % C == 0:
        cnt += A[i]//C
    else:
        cnt += (A[i]//C)+1

print(cnt)
