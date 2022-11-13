import sys
input = sys.stdin.readline

N, K = map(int, input().split())

pots = []

for _ in range(N):
    pots.append(int(input()))

left = 0
right = max(pots)

while left <= right:
    mid = (left+right)//2
    if mid == 0:
        break

    people = 0
    for pot in pots:
        people += pot//mid

    if people >= K:
        left = mid + 1
    else:
        right = mid - 1

print(right)
