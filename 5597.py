li = [0 for _ in range(30)]

for _ in range(30-2):
    n = int(input())
    li[n-1] = 1

for i in range(30):
    if li[i] == 0:
        print(i+1)
