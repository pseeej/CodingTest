from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
plans = deque(map(int, input().split()))
money = int(input())

plans = deque(sorted(plans))

limit = 1

while plans:
    if limit*N == money:
        print(limit)
        exit()

    if limit * N > money:
        break

    if limit >= plans[0]:
        money -= plans[0]
        N -= 1
        plans.popleft()

    limit += 1

print(limit-1)
