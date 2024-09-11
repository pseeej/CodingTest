from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
extds = defaultdict(int)

for _ in range(N):
    extd = input().split(".")[1].strip()
    extds[extd] += 1

sortedlist = sorted(extds.items(), key=lambda k:k[0])

for item in sortedlist:
    print(f"{item[0]} {item[1]}")
