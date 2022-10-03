import sys
input = sys.stdin.readline

N, L = map(int, input().split())
xs = list(map(int, input().split()))
centers = [0 for i in range(N+1)]

for i in range(1, N+1):
    centers[i] = (centers[i-1] + xs[i-1])

for i in range(1, N):
    calc = centers[N] - centers[N-i]
    calc /= i
    # print(xs[N-i-1]-L, xs[N-i-1]+L)
    if not (xs[N-i-1] - L < calc < xs[N-i-1] + L):
        print("unstable")
        exit()

print("stable")
