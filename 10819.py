from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
perms = list(permutations(nums, N))

res = []
tot = 0
for perm in perms:
    tmp = 0
    for i in range(1, N):
        tmp += abs(perm[i-1]-perm[i])

    if tmp > tot:
        res = perm
        tot = tmp

print(tot)
