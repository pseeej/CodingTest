import sys
input = sys.stdin.readline

n = int(input())

Hi = list(map(int, input().split()))
Ai = list(map(int, input().split()))

result = sum(Hi)
Ai.sort()

for i in range(n):
    result += Ai[i]*i

print(result)
