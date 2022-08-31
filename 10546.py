from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())

names = defaultdict(int)
for _ in range(N):
    name = input()
    names[name] += 1

for _ in range(N-1):
    name = input()
    names[name] -= 1

# 딕셔너리 정렬 작작 좀 까먹길
names = sorted(names.items(), key=lambda item:item[1], reverse=True)
print(names[0][0])
