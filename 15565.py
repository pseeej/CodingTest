import sys
input = sys.stdin.readline

N, K = map(int, input().split())
fluffies = list(map(int, input().split()))

ryan = []
for i in range(N):
    if fluffies[i] == 1:
        ryan.append(i)

start = 0
end = K-1
dist = 10**6

if len(ryan) < K:
    print("-1")
    exit()

while end < len(ryan):
    dist = min(dist, ryan[end] - ryan[start]+1)
    start += 1
    end += 1

print(dist)
