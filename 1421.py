import sys
from math import ceil
input = sys.stdin.readline

N, C, W = map(int, input().split())

trees = []

for _ in range(N):
    trees.append(int(input()))

result = 0

# i가 나무 길이
for i in range(1, max(trees)+1):
    calc = 0
    for tree in trees:
        calc += max(0, (tree//i) * i * W - ((ceil(tree/i)-1)*C))

    if calc > result:
        result = calc

print(result)
