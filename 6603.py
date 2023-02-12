import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    S = list(map(int, input().split()))
    K = S[0]
    if K == 0:
        break

    S = S[1:]
    combs = list(combinations(S, 6))

    for c in combs:
        print(*c)

    print()
