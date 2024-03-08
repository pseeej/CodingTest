# 15656
from itertools import product
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

tmp = list(product(nums, repeat=M))
tmp.sort()

for t in tmp:
    for n in t:
        print(n, end=" ")
    print()
