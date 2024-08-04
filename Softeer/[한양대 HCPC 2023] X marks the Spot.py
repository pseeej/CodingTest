import sys
input = sys.stdin.readline
num_words = int(input())
result = []

for i in range(num_words):
    x = list(map(str, input().split()))
    for j in range(len(x[0])):
        if x[0][j] in {"x", "X"}:
            result.append(x[1][j].upper())
            break
print(''.join(result))
