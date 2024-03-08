# 1431
import sys
input = sys.stdin.readline

N = int(input())
guitars = []
for _ in range(N):
    guitars.append(input().strip())

def checkSum(guit):
    result = 0
    for i in guit:
        if '0'<=i<='9':
            result += int(i)

    return result

result = sorted(guitars, key=lambda g:(len(g), checkSum(g), g))

for res in result:
    print(res)
