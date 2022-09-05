N = int(input())

ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort()

max_weight = 0
for i in range(N):
    calc = ropes[i]*(N-i)
    if max_weight < calc:
        max_weight = calc

print(max_weight)
