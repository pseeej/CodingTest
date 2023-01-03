import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())

maxsum = 0
maxidx = 0
for i in range(N):
    arr = list(map(int, input().split()))
    comb = list(combinations(arr, 3))
    for c in comb:
        temp = sum(c)
        if temp%10 >= maxsum:
            maxsum = temp%10
            maxidx = i+1

print(maxidx)
