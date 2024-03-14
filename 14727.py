from collections import defaultdict

N = int(input())
result = 0

for i in range(1, N+1):
    j = i
    while j < N+1:
        result += i
        j += i

print(result)
