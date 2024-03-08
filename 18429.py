from itertools import permutations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
kits = list(map(int, input().split()))

combs = list(permutations(kits, N))

result = 0
for comb in combs:
    curr = 500
    for kit in comb:
        curr += kit-K
        if curr < 500:
            break

    if curr >= 500:
        result += 1

print(result)
