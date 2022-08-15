from math import lcm
from itertools import combinations

nums = list(map(int, input().split()))
combs = list(combinations(nums, 3))

res = 999999
for c in combs:
    calc = lcm(c[0], c[1])
    calc = lcm(calc, c[2])

    if calc < res:
        res = calc

print(res)
