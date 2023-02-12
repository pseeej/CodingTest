import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
trees = []
for _ in range(N):
    trees.append(int(input()))

trees.sort()

dists = []
for i in range(1, N):
    dists.append(trees[i]-trees[i-1])

dist = gcd(*dists)

result = 0
for i in range(1, N):
    if trees[i]-trees[i-1] > dist:
        result += (trees[i]-trees[i-1])//dist - 1

print(result)
